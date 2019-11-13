

#operator trójargumentowy

def max_of_2(first, second):
    return first if first > second else second

def maximum_of(a, b, c):
    return max_of_2(max_of_2(a, b), c)

def read_value():
    return int(input("Put integer value: "))

x = 3
y = 8
z = 2

result = maximum_of(x, y, z)
print("Max of:", x, y, z, "is", result)


#1 metoda

def maximum_of(a, b, c):
    max_ab = a if a > b else b #1 sposób zapisu/
    max_abc = max_ab if max_ab > c else c
    # a > b -> a > c -> a
    # a > b -> b > c -> b
    # a > b -> a > c -> c

    if a > b: #drugi sposób zapisu/ 1 metoda cd
       max_ab = a
    else:
        max_ab = b

    if max_ab > c:
        max_abc = max_ab
    else:
        max_abc = c

    return max_abc

x = 3
y = 8
z = 2

print(maximum_of(x, y, z))