#"""All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#MasterCard numbers either start with the numbers 51 through 55 or with the numbers
#2221 through 2720. All have 16 digits.
#American Express card numbers start with 34 or 37 and have 15 digits."""

# 4035300539804083 visa
# 5168441223630339 mastercard
# 371642190784801  american

#metody:

def is_visa(is_card, number):
    if not is_card == False:
        return False

    if (len(number) == 16 or len(number) == 13):
        if number[0] == "4":
            return True

def is_mastercard(is_card, number):
    if not is_card == False:
        return False

    if is_card and len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True

def is_americanexpress(is_card, number):
    if not is_card == False:
        return False

    if is_card and len(number) == 15:
        if number[0:2] in ("34", "37"):
            return True


#główna częśc programu:
card_number = input("Put your card number hear: ")

can_be_card_number = False


if len(card_number) < 13 or len(card_number) > 16:
    print("Wrong number")

else:
    if card_number.isdecimal(): #składa się z samych cyfr; można wykorzystac też isdigit()
        print("Can be card number")
        can_be_card_number = True
    else:
        print("Not a number")


if is_visa(can_be_card_number, card_number):
    print("I'm Visa")
elif is_mastercard(can_be_card_number, card_number):
    print("I'm mastercard")
elif is_americanexpress(can_be_card_number, card_number):
    print("I'm american express")
else:
    print("Not know card type")