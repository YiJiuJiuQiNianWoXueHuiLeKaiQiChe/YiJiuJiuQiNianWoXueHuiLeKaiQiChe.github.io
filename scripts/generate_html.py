import yaml
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

def load_members():
    with open('members.yml', 'r') as file:
        data = yaml.safe_load(file)
    return data['members']

def categorize_members(members):
    categorized = defaultdict(list)
    for member in members:
        category = member.get('category', 'normal')
        categorized[category].append(member)
    return dict(categorized)

def generate_html(members):
    categorized_members = categorize_members(members)
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('members_template.html')
    html_output = template.render(categorized_members=categorized_members)
    with open('dist/members.html', 'w+') as file:
        file.write(html_output)

if __name__ == "__main__":
    members = load_members()
    generate_html(members)
