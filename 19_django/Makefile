# Makefile
#!/bin/bash
SHELL := /bin/bash

shell:
	echo "source ~/.bashrc" >> ~/.bash_history
	poetry shell
	source ~/.bashrc

start: 
	poetry run python manage.py runserver

start_guni: install_guni
	export DJANGO_SETTINGS_MODULE=hello_django.settings
	poetry run gunicorn hello_django.wsgi

install_django:
	poetry add django
	
install_guni: install_django
	poetry add gunicorn --dev

update:
	sudo apt update

flask: install_flask # FLASK_APP=
	FLASK_APP=$(path_to_flask_app) FLASK_DEBUG=1 FLASK_ENV=development flask run

ENV: update#-> ENV_NAME=
	python3 -m venv $(name) && source $(name)/bin/activate && pip list
	echo "source ~/.bashrc" >> $(name)/bin/activate
	echo "source $(name)/bin/activate" >> ~/.bash_history
	source $(name)/bin/activate

install_flask:
	poetry add flask --dev
	poetry add flask-debugtoolbar --dev
# Makefile last line
# ignores existing files
.PHONY: test, start, flask_start