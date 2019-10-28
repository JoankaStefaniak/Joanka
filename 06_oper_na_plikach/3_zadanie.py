import random

def random_quote(cytaty):
    quote_for_today = random.choice(cytaty).strip()
    return quote_for_today.split('-')

def show(quote):
    print("Quote of the day is: ")
    print('*' * 100)
    print(quote[0].center(100))
    print(quote[1].center(100))
    print('*' * 100)


filename = "cytaty.txt"
with open(filename) as f:
    quotes = f.readlines()

for i in range(3):
    sentence = random_quote(quotes)
    print('-----')
    show(sentence)
