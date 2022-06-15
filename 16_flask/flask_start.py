from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import logging

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

toolbar = DebugToolbarExtension(app)

title = '99 бутылок чего-то стояло на столе, одна упала и разбилась.'
alist = range(1,100)

@app.route('/99-bottles')
@app.route('/99-bottles.html')
def show_list_of_bottles():
    return render_template('99-bottles.html', title=title, alist=alist)

@app.route('/user/<username>')
def show_user_profile(username):
    return username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return str(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return subpath


if __name__ == "__main__":
	app.run(debug=True)