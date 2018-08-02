from datetime import datetime, timedelta
from random import randint
import lorem

def format_date(date):
	return f'{date.year}-{date.month}-{date.day}'

def format_title(title):
	blog_title = title[:-1]
	blog_title = blog_title.lower()
	blog_title = blog_title.replace(' ', '-')
	return blog_title

now = datetime.now()

for _ in range(40):
	date = now - timedelta(randint(1, 365))
	title = lorem.sentence()
	body = lorem.text()
	s = f'---\nlayout: post\ntitle: "{title}"\n---\n\n{body}'

	with open(f'./_posts/{format_date(date)}-{format_title(title)}.md', 'w') as file:
		file.write(s)