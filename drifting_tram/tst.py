import jinja2
from os import environ
env = jinja2.Environment(
    loader=jinja2.PackageLoader('drifter', 'templates'),
    autoescape=jinja2.escape(['xml'])
)

template = env.get_template('vm_template.xml')
print template.render(vm_name='xenial-1', vm_memory=1048576, volume_storage=environ['HOME'])
