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

from __future__ import absolute_import, division, print_function, unicode_literals

import calendar, locale
from decimal import Decimal
from django.template.defaultfilters import floatformat, yesno, urlencode
from django.utils import timezone
import six

number_types = six.integer_types + (Decimal, float)

def jinja_date_filter(d, fmt = "%d/%b/%y %I:%M%p"):
	if not d:
		return ''
	d = timezone.template_localtime(d)
	
	if fmt == '%s':
		return calendar.timegm(d.utctimetuple())
	return d.strftime(fmt)

def jinja_fmt(fmt, *args, **kwargs):
	return fmt.format(*args, **kwargs)

def jinja_filter_empty(seq):
	if hasattr(seq, '__iter__'):
		return filter(None, seq)
	return seq

def currency_format(num):
	if not isinstance(num, number_types):
		num = 0
	return locale.currency(num, grouping = True)

def percent_format(num):
	if not isinstance(num, number_types):
		num = 0
	st = "{0:.5f}".format(num * 100).rstrip('0')
	parts = st.split('.')
	# zfill adds 0s on left, so reverse string twice using [::-1]
	dec = parts[1][::-1].zfill(2)[::-1]
	full = '.'.join([parts[0], dec])
	return full

def get_filters(jinja_env):
	return {
		# modified django date filter
		'date' : jinja_date_filter,
		
		# Django filters
		'floatformat' : floatformat,
		'yesno' : yesno,
		'urlencode' : urlencode,
		
		# simple string.format() because django/jinja is missing it
		'fmt' : jinja_fmt,
		
		# Locale dependant
		'currency' : currency_format,
		'filter' : jinja_filter_empty,
		'varlen_percent': percent_format
	}
