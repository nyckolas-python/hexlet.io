from pprint import pprint
from jinja2 import Template

cars = [
	{'model': 'Audi', 'price': 23500},
	{'model': 'BMW', 'price': 33500},
	{'model': 'Shkoda', 'price': 18500},
	{'model': 'Volvo', 'price': 28500},
	{'model': 'Pegout', 'price': 21500}
]

tpl = '''Список автомобилей:
{% for a in cs|sort(reverse=true, attribute='price') -%}
Цена {{ a['model'] }} = {{ a.price }} UDS
{% endfor %}'''
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

#  Все фильры доступны по ссылке ниже:
#  
#  https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters


# | sum(iterable, attribute=None, start=0)

tpl = "Суммарная цена автомобилей: {{ cs | sum(attribute = 'price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

tpl = "Самый дорогой автомобиль: {{ (cs | max(attribute = 'price')).model }} {{ (cs | max(attribute = 'price')).price }} USD"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

tpl = "Самый бюджетный автомобиль: {{ (cs | min(attribute = 'price')).model }} {{ (cs | min(attribute = 'price')).price }} USD"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

tpl = "Популярная марка авто: {{ (cs | random).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# Макроопределения
tpl = '''
{% macro input(name, value='', type='text', size=20) -%}
	<input type="{{type}}" name="{{name}}" value="{{value | e}}" size="{{size}}">
{%- endmacro %}
<p>{{input('username')}}
<p>{{input('email')}}
<p>{{input('password')}}
'''

tm = Template(tpl)
msg = tm.render()

print(msg)

# Макросы и вложенные макросы

persons = [
	{'name': 'Adam', 'age': 37, 'weight': 74},
	{'name': 'Nyckolas', 'age': 32, 'weight': 64},
	{'name': 'Michel', 'age': 42, 'weight': 84},
	{'name': 'Clarck', 'age': 47, 'weight': 94}
]

tpl = '''
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
	<li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
	<ul>
	<li>Age: {{user.age}}
	<li>Weigth: {{user.weight}}
	</ul>
{% endcall -%}
'''
tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)