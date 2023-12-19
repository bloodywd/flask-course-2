# Makefile
PORT ?= 8000

install:
	poetry install
dev:
	poetry run flask --app flask_course:app --debug run
