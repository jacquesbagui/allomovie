SERVICE_WEB = backend

all: build up

build:
	docker-compose build

up:
	docker-compose up -d

up-it:
	docker-compose up

down:
	docker-compose down

logs:
	docker-compose logs -f

migrate:
	docker-compose run --rm $(SERVICE_WEB) python manage.py migrate

makemigrations:
	docker-compose run --rm $(SERVICE_WEB) python manage.py makemigrations

syncdb:
	docker-compose run --rm $(SERVICE_WEB) python manage.py migrate --run-syncdb

test:
	docker-compose run --rm $(SERVICE_WEB) python manage.py test

shell:
	docker-compose run --rm $(SERVICE_WEB) python manage.py shell

prune:
	docker system prune -af

bash:
	docker-compose exec $(SERVICE_WEB) bash

createsuperuser:
	docker-compose run --rm $(SERVICE_WEB) python manage.py createsuperuser

init-test-data:
	docker-compose run --rm $(SERVICE_WEB) python manage.py loaddata initial_data

.PHONY: all build up up-it down logs migrate makemigrations syncdb test shell prune bash createsuperuser init-test-data
