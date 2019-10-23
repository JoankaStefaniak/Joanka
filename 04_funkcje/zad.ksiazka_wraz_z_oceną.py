def add_book(dict_books):
    counter = int(input("Ile ksiazek chcesz dodac:"))
    for i in range(counter):
        title = input("Podaj tytul ksiazki:")
        grade = input("Podaj ocenę:")
        dict_books[title] = grade

    return dict_books

def read_book_by_grade(libr): #books - lokalna nazwa na słownik
    g = input("Podaj ocene ksiazki, jaką chcesz przeczytać: ")
    if g in libr.values():
        for title, grade in libr.items():
            if grade == g:
                print(title, " - ocena", grade)

    else:
        print("Nie ma ksiązki o takiej ocenie")


books = add_book()
print(books)

read_book_by_grade(books)

