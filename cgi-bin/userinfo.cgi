#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

def values(fields):
  for value in fields:
    if value in form: print form[value].value + '<br />'

if __name__ == '__main__':
  print 'Content-Type: text/htmln'

if 'submit' and 'done' in form:
  values(('name', 'age', 'email'))
else:
  print 'if you were directed here in error please visit here.com'
