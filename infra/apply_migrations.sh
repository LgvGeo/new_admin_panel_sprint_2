docker compose exec api python manage.py migrate admin
docker compose exec api python manage.py migrate auth
docker compose exec api python manage.py migrate contenttypes
docker compose exec api python manage.py migrate sessions
docker compose exec api python manage.py migrate --fake movies