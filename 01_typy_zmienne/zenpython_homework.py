Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
zenpython = """"Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
>>> "Ilość słowa 'better':"
"Ilość słowa 'better':"
>>> (zenpython.count("better"), "'n")
(8, "'n")
>>> "Zen bez gwiazdek: \n")
SyntaxError: invalid syntax
>>> ("Zen bez gwiazdek: \n")
'Zen bez gwiazdek: \n'
>>> (zenpython.replace('*'), "'n")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    (zenpython.replace('*'), "'n")
TypeError: replace() takes at least 2 arguments (1 given)
>>> (zenpython.replace('*', ''), "'n")
('"Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren\'t special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you\'re Dutch.\nNow is better than never.\nAlthough never is often better than right now.\nIf the implementation is hard to explain, it\'s a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let\'s do more of those!', "'n")
>>> ("Zen z jednym zmienionym 'explain' na 'understand': \n")
"Zen z jednym zmienionym 'explain' na 'understand': \n"
>>> (zenpython.replace("explain","understand", 1), "\n")
('"Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren\'t special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you\'re Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to understand, it\'s a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let\'s do more of those!', '\n')
>>> ("Zen bez spacji, ale z myslnikami: \n")
'Zen bez spacji, ale z myslnikami: \n'
>>> (zenpython.replace(" ", "-"), "\n")
('"Beautiful-is-better-than-ugly.\nExplicit-is-better-than-implicit.\nSimple-is-better-than-complex.\nComplex-is-better-than-complicated.\nFlat-is-better-than-nested.\nSparse-is-better-than-dense.\nReadability-counts.\nSpecial-cases-aren\'t-special-enough-to-break-the-rules.\nAlthough-practicality-beats-purity.\nErrors-should-never-pass-silently.\nUnless-explicitly-silenced.\nIn-the-face-of-ambiguity,-refuse-the-temptation-to-guess.\nThere-should-be-one---and-preferably-only-one---obvious-way-to-do-it.\nAlthough-that-way-may-not-be-obvious-at-first-unless-you\'re-Dutch.\nNow-is-better-than-never.\nAlthough-never-is-often-better-than-*right*-now.\nIf-the-implementation-is-hard-to-explain,-it\'s-a-bad-idea.\nIf-the-implementation-is-easy-to-explain,-it-may-be-a-good-idea.\nNamespaces-are-one-honking-great-idea----let\'s-do-more-of-those!', '\n')
>>> ("Zen podzielony:")
'Zen podzielony:'
>>> (zenpython.split(.))
SyntaxError: invalid syntax
>>> (zenpython.split('.'))
['"Beautiful is better than ugly', '\nExplicit is better than implicit', '\nSimple is better than complex', '\nComplex is better than complicated', '\nFlat is better than nested', '\nSparse is better than dense', '\nReadability counts', "\nSpecial cases aren't special enough to break the rules", '\nAlthough practicality beats purity', '\nErrors should never pass silently', '\nUnless explicitly silenced', '\nIn the face of ambiguity, refuse the temptation to guess', '\nThere should be one-- and preferably only one --obvious way to do it', "\nAlthough that way may not be obvious at first unless you're Dutch", '\nNow is better than never', '\nAlthough never is often better than *right* now', "\nIf the implementation is hard to explain, it's a bad idea", '\nIf the implementation is easy to explain, it may be a good idea', "\nNamespaces are one honking great idea -- let's do more of those!"]
>>> 
