numbers = [1,2,3, (10,20), 4, 5]
counter = 0
for n in numbers:
    if isinstance(n, tuple): #typ
        break
    else:
        counter = counter + 1 #counter +=

print(counter)



