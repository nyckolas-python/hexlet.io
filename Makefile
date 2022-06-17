# Makefile
#!/bin/bash
SHELL := /bin/bash

flask:
	FLASK_APP=./16_flask/flask_start.py FLASK_DEBUG=1 FLASK_ENV=development flask run

ENV:#-> ENV_NAME=
	python3 -m venv $(name) && source $(name)/bin/activate && pip list
	echo "source ~/.bashrc" >> $(name)/bin/activate
	echo "source $(name)/bin/activate" >> ~/.history
	source $(name)/bin/activate
	
guni:
	pip install gunicorn

# Makefile last line
# ignores existing files
.PHONY: test, start, flask_start