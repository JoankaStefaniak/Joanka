counter = int(input('Ile liczb dodać?:'))

elements = []
for i in range(counter): #zamiast i może być _ - to znaczy, że nie potrzebuijemy tej zmiennej
    e = input('Podaj element:')
    elements.append(e)
    #zapytaj o kolejną liczbe i potem dorzuć liczbę na listę

print(elements)
print('Czy pierwszy i ostatni są takie same', elements[0] == elements[-1])

if elements[0] == elements[-1]:
    print('Pierwszy i ostatni sa takie same')
else:
    print('Elementy nie są takie same')

elements2 = []
counter2 = 5
while(counter != 0):
    e = input()
    elements2.append(e)
    counter2 -= 1 #liczba bedzie sie zmniejszac o 1

print(elements2)


num_arr = []
while True:
    e = input('Podj nowy element. Nacisnij Q aby zakonczyc':)
    if e == "Q":
        break
    num_arr.append(e)

print(num_arr)