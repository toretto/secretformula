#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
cgitb.enable()

print "Content-Type: text/html;charset=utf-8"
print
print """\

<html>
<head>
<title>Shit</title>
</head>
<body>
<h2>Result</h2>
<p>
"""
#var1 = 2
#var2 = 4
#var3 = var1 + var2
#print var3
#print """\
form = cgi.FieldStorage() 
#instantiate only once!
prijs = int(form.getfirst('prijs','empty'))
korting = int(form.getfirst('korting','empty'))
#prijs = cgi.escape(prijs)
#korting = cgi.escape(korting)
totaal = prijs * ( 1.0 - (korting / 100.0))
print totaal
print """\
</p>
"""