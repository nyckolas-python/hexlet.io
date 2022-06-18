# Makefile
#!/bin/bash
SHELL := /bin/bash

flask:
	FLASK_APP=./16_flask/flask_start.py FLASK_DEBUG=1 FLASK_ENV=development flask run

ENV: update#-> ENV_NAME=
	python3 -m venv $(name) && source $(name)/bin/activate && pip list
	echo "source ~/.bashrc" >> $(name)/bin/activate
	echo "source $(name)/bin/activate" >> ~/.bash_history
	source $(name)/bin/activate

install_flask:
	pip install flask
	pip install flask-debugtoolbar 
	
guni: install_flask
	pip install gunicorn

update:
	sudo apt update
	sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools


# Makefile last line
# ignores existing files
.PHONY: test, start, flask_start