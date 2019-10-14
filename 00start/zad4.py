Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> center(***[mata])
SyntaxError: invalid syntax
>>> center(*[mata])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    center(*[mata])
NameError: name 'center' is not defined
>>> center(mata)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    center(mata)
NameError: name 'center' is not defined
>>> text = 'goahead'
>>> text.upper()
'GOAHEAD'
>>> nr = "2154538484736363"
>>> nr.isdecimal()
True
>>> txt = mata
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    txt = mata
NameError: name 'mata' is not defined
>>> text = mata
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    text = mata
NameError: name 'mata' is not defined
>>> txt = 'mata'
>>> txt.center(10)
'   mata   '
>>> txt.center(3, '*')
'mata'
>>> txt.center(3, "*")
'mata'
>>> url = "www.flynerd.pl"
>>> url.lstrip('www.')
'flynerd.pl'
>>> url.rstrip('.pl)
	   
SyntaxError: EOL while scanning string literal
>>> txt = "www.flynerd.pl"
>>> url.rstrip(".pl")
'www.flynerd'
>>> txt = "phoBar"
>>> txt = "fooBar"
>>> txt.isalpha()
True
>>> txt.isalpha() and not txt.islower()
True
>>> txt = "banana"
>>> txt.count("na")
2
>>> 
