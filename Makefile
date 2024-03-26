
all: start migrate migrations build run
	
	
start:
	docker compose --env-file .env up -d

migrations:
	docker compose --env-file .env run --rm app sh -c 'cd src && alembic revision --autogenerate -m "$(name)"'

migrate:
	docker compose --env-file .env run --rm app sh -c 'cd src && alembic upgrade head'

build:
	docker-compose build
	
run:
	docker-compose up

downgrade:
	docker compose --env-file .env run --rm app alembic downgrade -1