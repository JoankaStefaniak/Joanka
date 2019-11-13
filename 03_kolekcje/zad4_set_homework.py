example =  [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

list_1 = []
list_2 = []
list_3 = []

for i in example:
    if example.index(i) < int(len(example)/3):
        list_1.append(i)
    elif int(len(example)/3) <= example.index(i) < int(len(example)/3)*2:
        list_2.append(i)
    else:
        list_3.append(i)

print(list_1)
print(list_2)
print(list_3)

list_1.reverse()
list_2.reverse()
list_3.reverse()

print(list_1)
print(list_2)
print(list_3)