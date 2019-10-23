def add_book(dict_books):
    counter = int(input("Ile ksiazek chcesz dodac:"))
    for i in range(counter):
        title = input("Podaj tytul ksiazki:")
        grade = input("Podaj ocenę:")
        dict_books[title] = grade

    print(dict_books)



books = {}
books = add_book(books)
print(books)

 #counter liczy ksiązki
