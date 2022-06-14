<!DOCTYPE html>
<html>
<head>
	<title>{% block title %}{% endblock %}</title>
</head>
<body>
{%- block content -%}
	{% block table_content -%}
	<ul>
	{%- for li in table_list -%}
	{# параметр scoped расширяет область видимость для li#}
	<li>{% block item scoped %}{{ li }}{% endblock -%}
{% endfor %}
</ul>
	{% endblock table_content %}
{%- endblock content %}
</body>
</html>