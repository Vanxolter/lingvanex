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
