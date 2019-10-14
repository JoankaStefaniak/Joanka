p = 1
while(p <= 3):
    przedmiot = input("Podaj przedmiot")
    ocena = input("Ocena")
    print(przedmiot,"-", ocena)
    p = p+1


przedmioty = input('podaj przedmioty podzielone myslnikiem')
oceny = input('podaj oceny podzielone myslnikiem')
przedmioty = przedmioty.split('-')
oceny = oceny.split("-")

licznik = 0
#print(przedmioty[0])

while licznik < 3:
    print(przedmioty[licznik], "-" oceny[licznik])
    licznik = licznik + 1


