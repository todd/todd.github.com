---
layout: post
title: Breaking Ground with Shovel
published: true
category: 
tags: [shovel, seomoz, python, jekyll]
---

I recently made the decision to migrate off of Tumblr and start hosting my own blog. Initially, I was going to write my own and host it on one of my VPSs, but my limited time and other coding endeavors made that a project I was unlikely to finish anytime soon. So, instead, I opted for [Jekyll](https://github.com/mojombo/jekyll) and [GitHub Pages](http://pages.github.com) - this gave me the freedom of rolling a blog that still felt like my own while removing 75% of the development work I would have had to endure otherwise.

And it's awesome - I'm really enjoying it.

But, there's a little bit of boilerplate that has to go into every post - not to where it becomes a massive undertaking to draft one, but enough that it gets a little tedious. A glance at various Jekyll implementations revealed that many users are using a Rakefile to handle the monotonous task of creating new content and generating the associated boilerplate. Well, given that Python is my language of choice at the moment, I thought this would be a good opportunity to teach myself something new (and avoid the temptation of being lazy and cloning someone's Rakefile).

Enter [Shovel](https://github.com/seomoz/shovel). I first became aware of Shovel a few weeks ago when a weekly Python digest I receive made mention of it. Billed as "Rake for Python," I became intrigued and poked through the repo for a few minutes before filing it away in my mind and went back to work. When the inspiration for writing a task automator for Jekyll struck me, I decided I'd use this library instead of Rake.

To get started, I simply invoked `pip install shovel` (in a virtualenv, of course). You could also clone it from GitHub and then install it (note that, at minimum, you'll need `argparse` installed):

	git clone https://github.com/seomoz/shovel.git
	cd shovel
	python setup.py install

Once I had it installed, I got to work. Shovel will automatically execute a specified task in any file called `shovel.py` when `shovel <taskname>` is called in the same directory. Alternatively, you can "modularize" (this isn't strict Python modularization - see the [docs](https://github.com/seomoz/shovel/blob/master/README.md) for a more thorough explanation) your tasks by creating a `shovel` directory and creating Python files and/or subdirectories within it. For instance, if you had a task called `cure` in a file named `cancer.py` within a directory named `diseases`, you'd invoke it from the directory containing the `shovel` directory with `shovel diseases.cancer.cure`.

To start hacking with Shovel, you only need to import one class:

	from shovel import task

`task` is actually a decorator class - to use it, simply decorate a method with `@task` and it instantly becomes a task you can execute with Shovel (provided it's in a Shovel file or directory). So you can basically take any method you've written, wrap it with `@task`, and invoke it from the command line. Shovel will also look for arguments in the command to use as `args` or `kwargs` and uses comment blocks within the method as help dialogue (accessed, conveniently enough, with `shovel help`). These features make Shovel extremely easy and useful to use.

With this knowledge in hand, I set out to create a Shovel file that would handle my Jekyll dirty work. Beyond those two additional lines of code, there's nothing extra you need to add to get Shovel to work with your code (besides maybe making errors exit to the command line gracefully). From there it was a bunch of string and date manipulation to get the results I desired - what follows is one of my Shovel tasks for creating a blog post (a link to the full source is below that) - `CONFIG` references a list instantiated outside the method:
	
	{% highlight python %}
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
	{% endhighlight %}

The full source is available as a [gist](https://gist.github.com/2348706) (for easy cloning) or in the [repo](https://github.com/toddward/toddward.github.com/blob/master/shovel.py) that hosts this blog.

Shovel has some other interesting functionality that I won't go into here - I highly suggest you go check out the [Shovel repo](https://github.com/seomoz/shovel), read the documentation, and get started with it if you find it useful - it couldn't be easier to use.
