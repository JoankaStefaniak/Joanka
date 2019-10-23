def calc_bmi(weight, height):
    return weight / height ** 2

def bmi_status(bmi):
    if bmi < 19:
        print('niedowaga')
    elif bmi < 25:
        print('waga normalna')
    elif bmi < 30:
        print('nadwaga')
    else:
        print('otyłość')

h = 1.60
w = 60

bmi = round(calc_bmi(w, h), 4)
print(bmi)
bmi_status(bmi)

