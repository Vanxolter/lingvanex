Парсинг Lingvanex
========

About
-----
Author: Maksim Laurou <Lavrov.python@gmail.com>

------------------

**ЗАПУСК ПРОЕКТА**

1) Клонируем репозиторий: ''' git clone git@github.com:Vanxolter/lingvanex.git '''

2) Создаем виртуальное окружение:  ''' virtualenv -p python3 --prompt=lingva- venv/ '''

3) Устанавливаем необходимые библиотеки: ''' pip install -r requirements.txt '''

4) Создаем базу данных:
	  '''
      sudo su postgres
	  psql
	  CREATE USER lingva WITH PASSWORD 'lingva' CREATEDB;
	  CREATE DATABASE lingva OWNER lingva;
	  GRANT ALL PRIVILEGES ON DATABASE lingva TO lingva;
      '''

5) Поднимаем миграции:  ''' python manage.py migrate '''

6) Запускаем проект:  ''' python manage.py runserver '''

------------------

Результаты
-----
Страница с пустой базой данных до скрапинга
![result 1](https://github.com/Vanxolter/lingvanex/blob/521f5c592d4facca1872a63023dc90e9514e168a/parseapp/screens/1.png)  

Процесс скрапинга, ошибки чтения возникают при медленной прогрузке страницы при помощи selenium.
При возникновении ошибки, мы повторно перезагружаем страницу и пока не достанем нужные данные, цикл будет повторяться
![result 2](https://github.com/Vanxolter/lingvanex/blob/521f5c592d4facca1872a63023dc90e9514e168a/parseapp/screens/2.png)  

Отображение таблицы с данными, здесь я достал 30 приложений, чему свидетельствует пагинация по 3-ем страницам
![result 3](https://github.com/Vanxolter/lingvanex/blob/521f5c592d4facca1872a63023dc90e9514e168a/parseapp/screens/3.png)  

Сортировка по году, видим что изначально показываются более старые приложения
![result 4](https://github.com/Vanxolter/lingvanex/blob/521f5c592d4facca1872a63023dc90e9514e168a/parseapp/screens/4.png)  

Сортировка работает на каждой странице отдельно
![result 5](https://github.com/Vanxolter/lingvanex/blob/521f5c592d4facca1872a63023dc90e9514e168a/parseapp/screens/5.png)  

Фильтирация по полному названию компании (по частичному названию не была реализована)
![result 6](https://github.com/Vanxolter/lingvanex/blob/521f5c592d4facca1872a63023dc90e9514e168a/parseapp/screens/6.png)  
