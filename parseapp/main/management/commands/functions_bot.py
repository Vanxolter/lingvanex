from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from datetime import datetime
import traceback
from django.core.management.base import BaseCommand
from main.models import Parse_data


class Command(BaseCommand):

    help = "Запуск парсера через консоль - python manage.py functions_bot"

    def handle(self, *args, **options):
        def errors_log(info, main_info):

            """
			Кэширование ошибок в файлы
			:param info: Информация по ошибке
			:return: none
			"""

            date_time = datetime.today()
            only_date = datetime.time(date_time)
            with open(f"errors/error_{only_date.hour}_{only_date.minute}.txt", "w") as file:
                file.write(main_info)
                file.write(info)

        def save_main_page(url, name, *args):

            """
			Фунция чтения и сохранения HTML кода в файлы
			:param url: URL основной страницы
			:param name: Имя для нашего файла с HTML-кодом
			:param args: при вызове этой функции из функции 'start()' здесь хранится - True, при вызове из 'fishing_main_data' -
			False
			:return: Вызывает get_links() или просто возвращает путь к файлу с HTML-кодом
			"""

            start_time = time.time()
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.set_page_load_timeout(15)
            path_to_page = f"data/html_pages/page_code_of_{name}.html"

            try:
                driver.get(url)
                if args:
                    for i in range(9): # Прокручиваем страницу 9 раз пока не достанем 200 аппак
                        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                        time.sleep(1.5)
                else:
                    timeout = 10
                    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'breadcrumb'))
                    WebDriverWait(driver, timeout).until(element_present)
                    try:
                        """Если на странице есть кнопка с контактами - жмем ее для получения доп. HTML-кода"""
                        driver.find_element(By.ID, 'contactInfoButton_responsive').click()
                    except FileNotFoundError as _ex:
                        main_info = "Функ. save_main_page(), стр.64"
                        errors_log(traceback.format_exc(), main_info)
                    finally:
                        ...

            except Exception as _ex:
                main_info = "Функ. save_main_page(), стр.72"
                errors_log(traceback.format_exc(), main_info)

            finally:
                src = driver.page_source
                with open(path_to_page, "w") as file:
                    file.write(src)

                driver.close()
                driver.quit()
                print("--- %s seconds ---" % (time.time() - start_time))
                print(f"Page {name} is safe successfully")

                if args:
                    return get_links(path_to_page)
                else:
                    return path_to_page

        def get_links(path_to_page):
            """
			Функция для сбора ссылок с основной страницы, вызывается из save_main_page
			:param path_to_page: Путь к файлу с HTML-кодом основной страницы
			:return:
            """
            path_to_json = "data/jsons/all_links.json"
            short_url = "https://apps.microsoft.com/"

            try:
                with open(f"{path_to_page}", "r") as file:
                    src = file.read()

                soup = BeautifulSoup(src, "html.parser")
                all_apps = soup.find(id="all-products-listall-list-container").find_all(
                    class_="product_card_title title")
                all_links = {}

                for item in all_apps:
                    label = item.find(class_="title-span").text
                    link = "https://apps.microsoft.com" + f"{item.get('href')}"
                    all_links[label] = link

                with open(path_to_json, "w") as file:
                    json.dump(all_links, file, indent=4, ensure_ascii=False)

            except Exception as _ex:
                main_info = "Функ. get_links(), стр.121"
                errors_log(traceback.format_exc(), main_info)

            finally:
                print("Json is safe successfully")
                return fishing_main_data(path_to_json)

        names = []

        def fishing_main_data(path_to_json):
            """
            Функция для сбора сбора требуемых данных со страницы, вызывается из get_links
            :param path_to_json: путь json файлу с собранными ссылками
            :return:
            """

            try:
                with open(path_to_json, "r") as file:
                    all_links = json.load(file)
            except FileNotFoundError:
                main_info = "Функ. fishing_main_data(), стр.137"
                errors_log(traceback.format_exc(), main_info)

            for name, link in all_links.items():
                if name in names:
                    continue
                else:
                    path_to_page = save_main_page(link, name)

                    with open(f"{path_to_page}", "r") as file:
                        src = file.read()

                    soup = BeautifulSoup(src, "html.parser")
                    try:
                        name = soup.find(class_="breadcrumb").find("a", {"index": "2"}).text
                        names.append(name)
                        name_company = soup.find(id="publisherHeader_desktop").find_next_sibling().next_element.text
                        year = soup.find(id="versionHeader_desktop").find_next_sibling().text
                        Parse_data.objects.update_or_create(
                            link=link, name_app=name, name_company=name_company, release_year=year
                        )
                        print("------------------------------")
                        print(name)
                        print(name_company)
                        print(year)

                    except AttributeError:
                        print(f"Ошибка чтения____{name}")
                        fishing_main_data(path_to_json)

                    finally:
                        try:
                            contacts = soup.find(id="closeButton").find_next_sibling().find("a").text
                            Parse_data.objects.filter(name_app=name).update(email=contacts)
                            print(contacts)
                        except AttributeError as _ex:
                            main_info = "Кнопки контакта нет. Функ. save_main_page(), стр.159"
                            errors_log(traceback.format_exc(), main_info)
                        finally:
                            print(len(names))

        def start():
            """
            Функция запуска
            :return: Вызывает save_main_page()
            """
            url = "https://apps.microsoft.com/store/category/Business"
            name = url.split('/')[-1]  # Создаем имя для нашего HTML-файла с основной страницы
            save_main_page(url, name, True)

        start()
