'''
This is a Shovel (https://github.com/seomoz/shovel) script
that will create new Jekyll content and automatically
generate the YAML Front Matter boilerplate.
'''

import datetime
import os.path
import re
import sys

from shovel import task

CONFIG = {
	'layouts': '_layouts',
	'posts': '_posts',
	'post_ext': 'md'
}

@task
def post(title='new-blog-post', date=None):
	'''Creates a new blog post.
    
	Usage: shovel post --title "New Post" [--date "2012-4-3"]'''
	if not os.path.exists(CONFIG['posts']):
		sys.exit('shovel failed: ' + CONFIG['posts'] + ' is not a valid directory.')
    
	slug = re.sub(r'[^\w-]', '', title.lower().strip().replace(' ', '-'))
	if date and not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date):
		sys.exit('shovel failed: date must be in YYYY-MM-DD format. Please try again.')
	elif not date:
		date = datetime.datetime.now().strftime('%Y-%m-%d')
	filename = ''.join([CONFIG['posts'], '/', date, '-', slug, '.', CONFIG['post_ext']])
	if os.path.exists(filename):
		sys.exit('shovel failed: ' + filename + ' already exists. Please try again.')
    
	print 'Creating new post: ' + title
	with open(filename, 'w') as f:
		f.write('---\n')
		f.write('layout: post\n')
		f.write('title: ' + title + '\n')
		f.write('published: false\n')
		f.write('category: \n')
		f.write('tags: []\n')
		f.write('---')

@task
def page(title, name=None):
	'''Creates a new page.
	
	Usage: shovel page --title "New Page" [--name "new-page"]'''
	if not name: tmp = title 
	else: tmp = name
	name = re.sub(r'[^\w-]', '', tmp.lower().strip().replace(' ', '-'))
	name += '.' + CONFIG['post_ext']
	if os.path.exists(name):
		sys.exit('shovel failed: ' + name + ' already exists. Please try again.')
	print 'Creating new page: ' + title
	with open(name, 'w') as f:
		f.write('---\n')
		f.write('layout: page')
		f.write('title: "' + title + '"\n')
		f.write('---\n')