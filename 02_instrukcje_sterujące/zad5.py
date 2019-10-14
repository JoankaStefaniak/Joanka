password = input("Gimme password: ")
alphanum = password.isalnum()
condition_1_upper = alphanum and password.islower() # sa alfanumeryczne i nie są wszystkie małymi literami

if len(password) < 8:
    print("Password is too short. Should be 8 chars")
if not password.isalnum(): #nie skalda sie z cyfr i liter
    print("Your past should be alphanumeric")
if password.isalpha(): # alfanumeryczne
    print('Should contain digits too')
if password.isdigit():
    print('Should contain letters too')
if condition_1_upper:
    print('Should contain at least 1 upper')

print("End")



