# dopóki temperautra  = 200 rób
# zmienna która przechowuje celcjusze
# = wzór na C z temp F
# wyswietl (temp F, = ,temp C)
# aktualizuj temp F

temp_f = 0

while temp_f <= 200: #dopóki nie 200 st F
    temp_c = round(5/9 * (temp_f - 32), 2) # wyliczenie st C + zaokrąglenie do 2 miejsc po przecinku
    print(temp_f, "F = ", temp_c, "C")
    temp_f = temp_f + 20 #aktualizacja
