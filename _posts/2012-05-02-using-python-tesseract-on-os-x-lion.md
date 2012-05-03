---
layout: post
title: Using python-tesseract on OS X Lion
published: false
category: 
tags: [os x, tesseract, python, python-tesseract]
---
So I started a [new job](http://www.gopago.com) on Monday and have been interested in getting up and running with optical character recognition (OCR) libraries. [Tesseract]() seems to be the de facto "go-to" software for OCR and I wanted to get up and running with it and some [Python bindings](). As I found out, this is actually easier said than done and requires a very minor hack that I haven't found documented anywhere on the web.

Before we begin, note that I installed Tesseract and its dependencies with [Homebrew](). These instructions may work for MacPorts installs, but I haven't tested that - your mileage may vary.

Installing Tesseract (and its dependencies) was as simple as cracking open terminal and running `brew install tesseract`. You'll also want to make sure you have Swig installed - if you don't, run `brew install swig`. Next I had to get a python-tesseract [tarball]() to build. I'm a big fan of `virtualenv` and I use it for basically every little thing I do with Python - I set up a new one with `virtualenv tesseract_test`. I ran `source bin/activate` in my new virtualenv and then untarred the python-tesseract archive. Then I ran, as suggested by the [build docs](), `python setup.py build` and was greeted with this piece of wonderful news:

	include path=/opt/local/include
	Current Version : 0.7
	running build
	running build_py
	file tesseract.py (for module tesseract) not found
	file tesseract.py (for module tesseract) not found
	running build_ext
	building '_tesseract' extension
	swigging tesseract.i to tesseract_wrap.cpp
	swig -python -c++ -I/opt/local/include/tesseract -I/opt/local/include -I/opt/local/include/leptonica -o tesseract_wrap.cpp tesseract.i
	tesseract.i:11: Error: Unable to find 'publictypes.h'
	tesseract.i:12: Error: Unable to find 'thresholder.h'
	tesseract.i:13: Error: Unable to find 'baseapi.h'
	error: command 'swig' failed with exit status 1
	
I'm not the [only person]() who has run into this problem (which was the primary factor that motivated me to pen this). The build is failing because Swig can't find the right files - not because they don't exist, but because the setup script is looking in the wrong place. The fix for this is extremely simple - first, run `python setup.py clean`. Then open setup.py in your favorite editor and, on line 10, change

	prefix="/opt/local"
	
to

	prefix="/usr/local"
	
Save and exit. Homebrew, by default, symlinks software it installs into /usr/local - the setup script was looking for them in /opt/local instead. Changing this will correct that issue. Try running `python setup.py build` again. It should complete successfully this time and you can then run `python setup.py install` - you now have a working Python binding for Tesseract installed!

I hope this helps someone avoid the headscratching I endured for a little while trying to figure this out.