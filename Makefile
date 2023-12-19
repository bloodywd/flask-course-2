# Makefile
PORT ?= 8000

install:
	poetry install
dev:
	poetry run flask --app flask_course_2:app --debug run
db init:
	poetry run flask --app flask_course_2:app db init
migrate:
	poetry run flask --app flask_course_2:app db migrate -m 'add film model'
upgrade:
	poetry run flask --app flask_course_2:app db upgrade
