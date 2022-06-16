from urllib import response
from flask import Flask, render_template, make_response, request
from flask_debugtoolbar import DebugToolbarExtension
import logging

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

toolbar = DebugToolbarExtension(app)

title = 'Динамические URL. Сложный роутинг. Шаблонизация Jinja2. Query String. Request. Respose.'
alist = range(1,100)


'''
Задание:
1.	Добавьте обработчик в ваше приложение (путь выберите сами).
2.	Сделайте так, чтобы обработчик возвращал параметры запроса в виде JSON-объекта. Добейтесь того, чтобы ключи соответствовали именам параметров, а значения — спискам значений для каждого параметра (помним, в запросе параметр может встречаться несколько раз!).
Решение:
'''
@app.route('/json', methods=['GET', 'POST'])
def json():
    response = make_response()
    response.mimetype = 'application/json'    
    keys = request.args.keys()
    d = {k: request.args.getlist(k) for k in keys}
    return d


'''
Задание:
1.	Добавьте в ваше приложение маршрут /args.
2.	Реализуйте обработчик для этого маршрута, возвращающий HTML-страницу c таблицей.
3.	Выводите в таблицу имена и значения параметров из query string. Помните о том, что каждый параметр может иметь несколько значений.
Решение:
'''
@app.route('/args', methods=['GET', 'POST'])
def show_query_sring_args():
    return render_template('args.html', title=title)

'''
Задание:
1.	В созданном ранее Flask-приложении добавьте обработчик пути /99-bottles, который должен будет отдать HTML-страницу, построенную с помощью шаблонизатора.
2.	Сделайте так, чтобы страница содержала маркированный список <ul> c элементами <li>. Элементы должны содержать строки "99 бутылок чего-то стояло на столе, одна упала и разбилась.", "98 бутылок..." и так далее вплоть до "Нет больше бутылок на столе.". Вам пригодится цикл for в его шаблонной версии.
Решение:
'''
@app.route('/99-bottles')
@app.route('/99-bottles.html')
def show_list_of_bottles():
    return render_template('99-bottles.html', title=title, alist=alist)
'''
Сложный роутинг и формирование URL

Такие генерируемые URL проще читать, ведь вы указываете не путь, а имя обработчика.
К тому же если вы потом поменяете правила маршрутизации, вам не придётся менять URL — 
при генерации всегда используются актуальные маршруты! А ещё вам не придётся задумываться
об экранировании параметров или кодировании строк с Unicode-символами: url_for делает и это!
'''
@app.route('/')
def index():
    return 'index'# …

@app.route('/posts/', defaults={'page': 1})
@app.route('/posts/page/<int:page>')
def list_posts(page):
    return 'posts'# …

def get_urls():
    return [
        url_for('index'),                # '/'
        url_for('list_posts'),           # '/posts/'
        url_for('list_posts', page=42),  # '/posts/page/42'
    ]
    
'''
Динамические пути.
Статический путь становится динамическим, если в него включают "переменные" (variable sections).
Выглядит это так:
'''    
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