<p>Page content
	{% macro list_users(list_of_users) -%}
	<ul>
	{% for u in list_of_users -%}
		<li>{{u.name}} {{caller(u)}}
	{%- endfor %}
	</ul>
{% endmacro %}
	{% call(user) list_users(users) %}
		<ul>
		<li>Age: {{user.age}}
		<li>Weigth: {{user.weight}}
		</ul>
	{% endcall -%}
<p>END Page content