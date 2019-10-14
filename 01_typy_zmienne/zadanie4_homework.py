Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> ("Czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową \n")
'Czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową \n'
>>> title = input("Podaj tytuł: \n")
Podaj tytuł: 
surname = input("Podaj nazwisko autora: \n")
>>> surname = input("Podaj nazwisko autora: \n")
Podaj nazwisko autora: 
pages = input("Podaj liczbę stron: /n")
>>> pages = input("Podaj liczbę stron: /n")
Podaj liczbę stron: /n
>>> (title.isalpha(), surname.isalpha(), pages.isdigit())
(False, False, False)
>>> ("Pilnuję, by nazwiska i tytuły były z dużej litery:")
'Pilnuję, by nazwiska i tytuły były z dużej litery:'
>>> (title.capitalize())
'Surname = input("podaj nazwisko autora: \\n")'
>>> (surname.capitalize())
'Pages = input("podaj liczbę stron: /n")'
>>> ("Łączę dane w jeden ciąg za pomocą spacji: ")
'Łączę dane w jeden ciąg za pomocą spacji: '
>>> book = title.capitalize() + " " + surname.capitalize() + " "+ pages
>>> (book)
'Surname = input("podaj nazwisko autora: \\n") Pages = input("podaj liczbę stron: /n") '
>>> ("Liczba wszystkich znaków w 'book'")
"Liczba wszystkich znaków w 'book'"
>>> (len(book))
85
>>> 
