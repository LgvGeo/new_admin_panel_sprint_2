# Запуск проекта

Переходим в папку infra/docker-compose:  

Создаем .env файл с переменными окружения(пример)  
POSTGRES_USER=app  
POSTGRES_DB=movies_database  
POSTGRES_PASSWORD=123qwe  
DB_NAME=movies_database  
DB_HOST=db  
DB_USER=app  
DB_PASSWORD=123qwe  
DB_PORT=5432  
DEBUG=True  
SECRET_KEY=ll  
UWSGI_PROCESSES=1  
UWSGI_THREADS=16  
UWSGI_HARAKIRI=240  

выполняем команду sudo docker compose up --build  
После этого применяем миграции:  
sudo bash ../apply_migrations.sh  
Можно создать суперпользователя:  
sudo bash ../create_superuser.sh  


# Описание задания на 2 спринт
 
Описание структуры и порядок выполнения проекта:

1. `docker_compose` — задача про настройку Nginx, Docker и Django.
2. `django_api` — задача про реализацию API для выдачи информации о фильме.

Напоминаем, что все части работы нужно сдавать на ревью одновременно.

Успехов!

