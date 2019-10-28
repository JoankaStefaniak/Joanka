filename = 'pan_tadeusz.txt'

with open(filename) as fopen: #standard nazywania zmiennych "f"
    content = fopen.read() #readlines - linijka po linijce
    print(content)

print("Koniec!")

f = open(filename) #rozbudowana składnia content = (to wyżej)
print(f.read())
f.close