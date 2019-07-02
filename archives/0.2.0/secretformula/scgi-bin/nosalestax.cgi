#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
#Import Galleries
import cgitb
import cgi
cgitb.enable()

#Print document header and empty space. Mandatory
print "Content-Type: text/html;charset=utf-8"
print
#Start printing HTML
print """\

<html>
<head>
<title>Results</title>
	<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
	<link rel="stylesheet" href="../css/custom.css">
	<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<div class="jumbotron">
  <h1>Prijs zonder BTW</h1>
<p>
"""
#Back to python to print the values
#Load data from the form
form = cgi.FieldStorage() 
#instantiate only once!

#Get values from the fields named "prijs" en "korting"
prijs = float(form.getfirst('prijs','empty'))
vat = float(form.getfirst('vat','empty'))
#prijs = cgi.escape(prijs)
#korting = cgi.escape(korting)
totaal = prijs / ( 1.0 + (vat / 100.0))
#Write double % ("%%") to write % without error. Adding %s allows to define variables outside of text
print ("Zonder %s%% BTW op €%s is de nieuwe prijs €%s" % (vat,prijs,totaal))
#End of Python, back to writing HTML
print """\

</p>
<p><a href="http://toralkohost.com/calculate.html" class="btn btn-default">Back</a></span></p>
</div>
"""