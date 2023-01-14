from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import django
django.setup()
from main.models import Parse_data


class Command(BaseCommand):
    help = "Crawl apps.microsoft"

    def handle(self, *args, **options):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        time.sleep(2)

        driver.get("https://apps.microsoft.com/store/category/Business")

        for i in range(0):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(2)

        ides = driver.find_element(By.ID, "all-products-listall-list-container")
        ides2 = ides.find_element(By.CSS_SELECTOR, "div[role='row']")
        card = ides2.find_elements(By.XPATH, "//*[@class='product_card_title title']")
        urls = []
        for i in card:
            urls.append(i.get_attribute("href"))
            Parse_data.objects.update_or_create(
                link=i.get_attribute("href"), name_app="1",
            )
        print(urls)
        print(len(urls))



'''options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome()
time.sleep(2)

driver.get("https://apps.microsoft.com/store/category/Business")

for i in range(0):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

ides = driver.find_element(By.ID, "all-products-listall-list-container")
ides2 = ides.find_element(By.CSS_SELECTOR, "div[role='row']")
card = ides2.find_elements(By.XPATH, "//*[@class='product_card_title title']")
urls = []
for i in card:
    urls.append(i.get_attribute("href"))
    Parse_data.objects.update_or_create(
        link=i.get_attribute("href"), name_app="1",
    )
print(urls)
print(len(urls))'''


