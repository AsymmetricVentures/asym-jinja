# -*- coding: utf-8 -*-
#    Asymmetric Base Framework :: Jinja2 utils
#    Copyright (C) 2013-2014 Asymmetric Ventures Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from datetime import datetime
from setuptools import setup, find_packages

classifiers = """
Development Status :: 4 - Beta
Framework :: Django
Programming Language :: Python
Intended Audience :: Developers
Natural Language :: English
Operating System :: OS Independent
Topic :: Software Development :: Libraries
Topic :: Utilities
License :: OSI Approved :: GNU General Public License v2 (GPLv2)
Topic :: Software Development :: Libraries :: Application Frameworks
"""

version = '0.2.0'
url = 'https://github.com/AsymmetricVentures/asym-jinja'

setup(
	name = 'asymm-jinja',
	version = '{}-{}'.format(version, datetime.now().strftime('%Y%m%d%H%M')),
	url = url,
	download_url = '{}/archive/v{}.tar.gz'.format(url, version),
	description = 'Django-jinja glue code and custom filters/functions',
	author = 'Richard Eames',
	author_email = 'reames@asymmetricventures.com',
	packages = find_packages(),
	classifiers = list(filter(None, classifiers.split('\n'))),
	
	install_requires = (
		'django>=1.4.5',
		'jinja2>=2.7',
		'pytz',  # most recent
	),
	
	test_suite = 'run_tests.main'
)
