# Makefile
flask:
	FLASK_APP=./16_flask/flask_start.py FLASK_DEBUG=1 FLASK_ENV=development flask run

# Makefile last line
# ignores existing files
#.PHONY: test, start, flask_start