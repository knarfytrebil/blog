#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Relaed'
SITENAME = u"Cyanide"
SITEURL = ''
HIDE_SIDEBAR = True

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', '#'),
          ('Github', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'sandstone'
# HIDE_SIDEBAR = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
