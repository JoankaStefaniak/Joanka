import random

def ran_name():
    name_length = random.randint(3, 7)
    return name_length

def even(name_length):
    name_even = name_length % 2
    if name_even == 1:
        name_length = name_length + 1
    return name_length

def name_creator():
    indicator = (name_length / 2) + 1
    i = 1
    while i < indicator:
        cons = random.choice(list(consonants))
        vow = random.choice(list(vowels))
        name.append(cons)
        name.append(vow)
        i += 1
    return name

def blind_element(array): #ślepy element (losowy)
    element = random.choice(list(array))
    return element

def finding_the_killer(array):
    killer = random.choice(list(array))
    return killer

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "y", "z"]
vowels = ["a", "e", "i", "o", "u", "y"]
name = []
alias = ["manly", "combative", "resonable", "furious", "brave", "cunny", "fast", "old", "alluring"]
race = ["dwarf", "minotaur", "elf", "driad", "witch", "human", "ogre", "troll", "dragon", "siren"]
places = ["forest", "castle", "town", "cave", "seaside", "river", "pub", "dungeon", "king's chamber", "queens chamber"]
npcs = ["the Queen", "Royal knight", "maid", "suspicious traveller", "your mother"]
actions = ["reading books", "selling potions", "cleaning up", "eating chicken", "looking at the sky", "writting a letter"]


name_length = ran_name()
name_length = even(name_length)

name = name_creator()

final_name = "".join(name)
final_name = final_name.capitalize() #pierwsza wielka litera

final_alias = random.choice(list(alias))
final_race = random.choice(list(race))

warrior_name = "{name} the {alias} {race}".format(name=final_name, alias=final_alias, race=final_race)
print("Your warrior name is:", warrior_name)

#-------------------------------------------------------------

killer = finding_the_killer(npcs)

Intro = "\nHello {name}! Your king was killed and now you need to find the killer!\nYou have only 8 days to found out who killer your king! Otherwise he will kill you too!".format(name = warrior_name)
print(Intro)

i = 1
while i < 9:
    Place = blind_element(places)
    person = blind_element(npcs)
    Standard_plot = "\nYou go to {place} and meet there {person} who is {action}".format(place=Place,
                                                                                       person=person,
                                                                                       action=blind_element(
                                                                                           actions))
    print(Standard_plot)
    question = input("Is that personal a killer? [y/n]\n\t")
    if question == "y":
        if person == killer:
            print("You save the city!")
            break
        else:
            print("This person is not a killer. What a shame!")
    if i == 8:
        print("8 days have passed and you're getting killed!\n\t\tTHE END")
    i += 1

