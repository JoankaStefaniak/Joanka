with open('pan_tadeusz.txt') as fopen:
  while True:
    current_line = fopen.readline()

    # aktualna linia jest pusta
    if current_line == '':
      # dotarlismy do konca
      break
    print(current_line)

    #pętla while wyświetla się do końca


#----------------------------------------------

with open('pan_tadeusz.txt', 'r') as fopen:
  lines = fopen.readlines()

for l in range(len(lines)):
  print("Line " + str(l), lines[l])

# ----------------------------------------------

with open('pan_tadeusz.txt', 'r') as fopen:
  lines = fopen.readlines()

for l in lines:
  print("Line : " + l)

# ----------------------------------------------

filename = 'pan_tadeusz'

with open(filename) as fopen:
    list_of_lines = fopen.readlines()

for i in range(len(list_of_lines)):
    print('Linia {i}:', list_of_lines)

# ----------------------------------------------
print(list_of_lines)
print("-------------------")

for i in list_of_lines:
    print("Linia: ", i.strip)