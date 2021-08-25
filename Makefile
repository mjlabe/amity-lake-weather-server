.PHONY: build
build:
	docker build -t amity_lake_weather .

.PHONY: run
run:
	docker-compose down
	docker-compose up

.PHONY: makemigrations
makemigrations:
	@echo Migration name:
	@read line; docker-compose run web bash -c "alembic revision --autogenerate -m "$$line""

.PHONY: migrate
migrate:
	docker-compose run web bash -c "alembic upgrade head"
