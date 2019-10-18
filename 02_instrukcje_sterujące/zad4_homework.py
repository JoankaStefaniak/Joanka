ciag = input('Podaj dowolny ciąg znaków: \n')
dlugosc = len(ciag)
czy_ma_a = ciag.count('a')
print(czy_ma_a)

if dlugosc > 5:
    print('Ten ciag znaków ma więcej niż 5 znaków')
elif dlugosc == 5:
    print('Ten ciag znaków ma dokłądnie 5 znaków')
else:
    print('Ten ciag znaków ma mniej niż 5 znaków')

if czy_ma_a > 0:
    print("Zamien 'a' na 'z'!" , ciag.replace('a','z'))

else:
    print('Twoj ciag nie zawiera "a"')