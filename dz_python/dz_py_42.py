# Homework_42
from jinja2 import Template

lst = [
    {'id': 'index', 'name': 'Главная'},
    {'id': 'news', 'name': 'Новости'},
    {'id': 'about', 'name': 'О компании'},
    {'id': 'shop', 'name': 'Магазин'},
    {'id': 'contacts', 'name': 'Контакты'}
]

link = """
<ul>
    {%- for c in lst %}
        {% if c.name == 'Главная' -%}
            <li><a href='/{{ c['id'] }}' class='active'>{{ c['name'] }}</a></li>
        {% else -%}
            <li><a href='/{{ c['id'] }}'>{{ c['name'] }}</a></li>
        {% endif %}
    {%- endfor %}
</ul>
"""

tm = Template(link)
msg = tm.render(lst=lst)

print(msg)
