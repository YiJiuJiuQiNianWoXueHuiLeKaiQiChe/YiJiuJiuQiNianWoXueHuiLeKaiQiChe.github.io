import yaml
from jinja2 import Environment, FileSystemLoader

def load_members():
    with open('members.yml', 'r') as file:
        data = yaml.safe_load(file)
    return data['members']

def generate_html(members):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('members_template.html')
    html_output = template.render(members=members)
    with open('output/members.html', 'w+') as file:
        file.write(html_output)

if __name__ == "__main__":
    members = load_members()
    generate_html(members)
