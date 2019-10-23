dict = {}

wiersz = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

wiersz.list = wiersz.replace(',','').split()

for i in txt.list:
    if i.lower() in dict:
        dict[i.lower()] += 1
    else:
        dict[i.lower()] = 1

print(dict)