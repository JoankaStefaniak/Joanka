secret_num = 5
zadanie = int(input('Zgadnij liczbe ukrytą w programie: '))

while secret_num != zadanie:
    print('Liczba', zadanie, 'nie jest liczbą ukrytą w programie!')
    zadanie = int(input('Zgadnij liczbe ukrytą w programie: '))

    print('n\Tak! Zgadłeś!')
