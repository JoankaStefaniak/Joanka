import random

filename = input("Your file: ")  #otwieranie z pliku, który istnieje - dowolny, który poda user
with open(filename) as f:
    cytaty = f.readlines()

quote_for_today = random.choice(cytaty).strip() #losowanie
quote_for_today = quote_for_today.split('-')
print(quote_for_today)

print("Quote of the day is: ")
print('*'*100)
print(quote_for_today[0].center(100))
print(quote_for_today[1].center(100))
print('*'*100)





