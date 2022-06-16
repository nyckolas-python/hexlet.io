#!/bin/bash
SHELL=/bin/bash
# Makefile
flask:
	FLASK_APP=./16_flask/flask_start.py FLASK_DEBUG=1 FLASK_ENV=development flask run

ENV:
	python3 -m venv $(NAME) && source $(NAME)/bin/activate && pip list
	echo "If you want instal some package use: pip install <package_name>/n"
	echo "to activate your enviroment: source myvenv/bin/activate"

# Makefile last line
# ignores existing files
.PHONY: test, start, flask_start