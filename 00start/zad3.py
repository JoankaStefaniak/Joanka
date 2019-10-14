Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt = Stefaniak
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    txt = Stefaniak
NameError: name 'Stefaniak' is not defined
>>> txt = 'Stefaniak'
>>> len(txt)
9
>>> txt.count('fan *3)
	  
SyntaxError: EOL while scanning string literal
>>> txt.count('fan' * 3)
0
>>> txt[3:6]
'fan'
>>> txt = "ciastko"
>>> result = "ast"
>>> txt[2:5]
'ast'
>>> txt[2:5] == result
True
>>> len(txt)
7
>>> middle = len9txt)/2
SyntaxError: invalid syntax
>>> middle = len(txt)/2
>>> middle
3.5
>>> middle = len(txt)//2
>>> middle
3
>>> txt[middle - 1] + txt[middle] + txt[middle] + 1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    txt[middle - 1] + txt[middle] + txt[middle] + 1
TypeError: can only concatenate str (not "int") to str
>>> txt[middle - 1] + txt[middle] + txt[middle + 1]
'ast'
>>> txt[middle - 1 : middle + 2]
'ast'
>>> quote = 'Honesty is the first chapter in the book of wisdom.'
>>> quote.count('Honesty is the first chapter in the book of wisdom.')
1
>>> len(quote)
51
>>> quote.index[wisdom]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    quote.index[wisdom]
NameError: name 'wisdom' is not defined
>>> quote. 
