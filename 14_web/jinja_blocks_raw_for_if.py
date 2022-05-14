from jinja2 import Template
from markupsafe import escape

### Экранирование и блоки raw, for, if

#Экранирование блоков
data = '''{% raw %}Модуль Jinja вместо
определение {{ name }}
подставить соответственное значение{% endraw %}

'''
name = 'Nyckolas'
tm = Template(data)
msg = tm.render(name=name)
print(msg)

#Экранирование символов первый вариант
link = '''В HTML-документе ссылки определяются так:
<a href='#'>Сыылка</a>

'''
tm_link = Template("{{ link | e }}")
msg = tm_link.render(link=link)
print(msg)

#Экранирование символов лучший вариант
#from markupsafe import escape
msg = escape(link)
print(msg)

#Блок for

cities = [{'id': 1, 'city': 'Kyiv'},
{'id': 2, 'city': 'New York'},
{'id': 3, 'city': 'London'},
{'id': 4, 'city': 'Coppen'},
{'id': 5, 'city': 'Zinkiv'}]

# -% - убираетперенос строки
link = '''<select name="cities">
{% for c in cities -%}
	<option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''
tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
