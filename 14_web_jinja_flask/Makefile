# Makefile
flask_start: flask_option
	python3 -m flask run

flask_option:
	export FLASK_APP=flask_start.py
	export FLASK_ENV=development

# Makefile last line
# ignores existing files
#.PHONY: test, start, flask_start