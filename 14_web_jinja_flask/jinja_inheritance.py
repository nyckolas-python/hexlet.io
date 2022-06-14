from jinja2 import Environment, FileSystemLoader

subs = [1,2,3,4,5,6]

file_loader = FileSystemLoader('14_web/templates/')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(table_list=subs)

print(msg)