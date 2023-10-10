# "Хакатон Лента х Практикум сентябрь’23"

## _Команды Мастерских Яндекс Практикума и команда Ленты подготовили для вас хакатон, в рамках которого команды создают интерфейс и предсказательную модель по прогнозированию спроса на товары заказчика собственного производства._

### Задача:

создание предсказательной модели и его интерфейса по прогнозированию спроса на товары заказчика собственного производства ООО “Лента”.

<details><summary>Локальный запуск приложения пока не в контейнерах</summary><br>

Склонировать репозиторий на свой компьютер и перейти в корневую папку:
```
git clone git@github.com:dmsvalik/lenta_hackathon.git
cd lenta
python3 -m venv venv # установить виртуальный режим

# Linux/macOS:
  source venv/bin/activate
# windows:
  source venv/scripts/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
При успешном старте получим backend приложение на [127.0.0.1:8000](https://127.0.0.1:8000)
```
Для создания супер пользователя необходимо ввести команду - python manage.py createsuperuser
```
Для импорта товаров из данных заказчика - python manage.py imp_store_to_db <br>
Для импорта магазинов заказчика - python manage.py imp_sku_to_db <br>
Для импорта истории покупок - python manage.py imp_sales_to_db (!!!!!  Процесс долгий - 2 часа !!!!!)

```
Для просмотра документации - https://127.0.0.1:8000/redoc<br>
Swagger - https://127.0.0.1:8000/swagger

```


### Используемые технологии

Python 3.11.5, Django 4.2.5, Django REST Framework, sqlLite, Docker, nginx, gunicorn, flake8.

### Авторы проекта

[Мельник Вячеслав](https://github.com/dmsvalik)<br>
[Киселев Никита](https://github.com/10-42)

### Посмотреть готовый проект

К сожалению, только локально!!!
