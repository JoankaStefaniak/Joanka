dog = {
  'name': 'Pimpek',
  'breed': "sznaucer",
  'age': '4',
  'color': 'white'
}

import random #losowanie

class Dog:
    tail = True #globalna zmienna/atrybut

    def __init__(self, name, breed, age, color): #self jest tylko dla pythona /wysyłamy atrybuty
        self.name = name #/definiujemy atrybuty
        self.breed = breed
        self.age = age
        self.color = color

    def pseudo(self):
        adj = ["destroyer", "powerful", "funny", "crazy"]
        #return adj[-1] + "-" + self.name
        return self.name + "-" + random.choice(adj)

obj_pimpek = Dog("Pimpek", "Collie", "5", "white")
obj_dyzio = Dog("Dyzio", "Cotton", "4", "blond")

print(Dog.pseudo(obj_dyzio))

names = "Anna, Marta, Marek, Paweł"
print(names.split(",")) #sep="," / separator
print(type(names))

print(str.split(names))

# print(obj_pimpek.pseudo())

# print(obj_dyzio.pseudo())
# print(obj_pimpek.tail)
# print(obj_dyzio.name)
# print(obj_dyzio.__dict__)
# print(Dog.__dict__) # .tail - wspólny atrybut - można się do niego odwołać z poziomu klasy



# obj_pimpek = Dog() #object / nowy obiekt tworzymy przez ()
# obj_dyzio = Dog()
#
# obj_pimpek.name = "Pimpek" #stworzyliśmy zmienna dla klasy i nadaliśmy jej wartośc
# obj_pimpek.age = "4"
# obj_pimpek.color = "white"
# print(obj_pimpek.name)
# print(obj_pimpek.age)
# print(obj_pimpek.color)