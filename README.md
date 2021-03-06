# [Урок 2. Разворачиваем сайт локально](https://dvmn.org/modules/django-orm/lesson/django-installation)

## Пульт охраны банка
Пульт охраны это сайт, который можно подключить к удалённой БД с визитами и пропусками сотрудников банка.

Это внутренний репозиторий для сотрудников банка "Восход". Если вы попали в этот репозиторий случайно,
то не сможете его запустить, так как у вас нет доступа к БД, но можете свободно использовать код вёрстки
или посмотреть реализацию запросов к БД.

## Requirements
    django==3.2.*
    environs==9.5.0
    psycopg2-binary==2.9.*
    python-dotenv==0.20.0

## Установка
    pip install -r requirements.txt

## Переменные окружения
Создайте в корне проекта файл `.env` и поместите в него следующие данные в формате `KEY=value`:
Или по правилам хостинга создайте переменные окружения.

`DBHOST=` - web-адрес точки подключения к БД, например `mysite.mydomain.ru`;

`DBPORT=` - порт сервера БД, например `1234`;

`DBNAME=` - имя БД;

`DBUSER=` - имя пользователя БД;

`DBPASS=` - пароль пользователя БД;

`DJANGO_SECRETKEY=` - секретный ключ Django;

`DEBUG=` - True для включения режима отладки, False - для production; 

`ALLOWED_HOSTS=` - список адресов через `,`.


## Запуск пульта охраны
Запуск пульта охраны производится командой `python manage.py runserver <server_address>:<port>`,
где:

`<server_address>` - адрес, по которому будет доступен сервер сайта;

`<port>` - порт сервера сайта.

### Пример команд запуска
    python manage.py runserver
    python manage.py runserver localhost:80
    python manage.py runserver 127.0.0.1:80
    python manage.py runserver 127.0.0.1:8000
