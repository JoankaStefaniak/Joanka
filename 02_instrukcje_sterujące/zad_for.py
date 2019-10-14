txt = 'bajlando' #zmienna musi byc w ''
for letter in txt:
    print("-", letter)

txt = 'bajlando'
for letter in txt: # letter to zmienna sterująca biorąca sekwencję i rozbijająca ją
    print(".", letter)

#in range - zakres

# range (start, stop, krok)


# for i in sekwencja/ sekwencja = tekst/ lista  np. ["Ala", "ma", "kota"]
# for step in range/ range = metoda (jedna liczba np. 1,2,3,4; ciąg np. 2-5, ciąg 2,10,3 (czyli 2,5,8)

for i in range(10, 30, 20):
    print(i)
    print(list(range(10,20, 30)))
    
