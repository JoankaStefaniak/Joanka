with open('ćwiczenie.txt', 'w') as f:
  f.write('Line 1')
  f.write('Line 2')
  f.write('Line 3')
  f.write('Line 4')

with open('ćwiczenie.txt', 'w') as f:   #zapis sformatowany
  f.write('Line 1\n')
  f.write('Line 2\n')
  f.write('Line 3\n')
  f.write('Line 4\n')
  f.write('The end!')

with open('save.txt', 'w', encoding='utf-8') as f:
  f.write('utf-8 text') #kodowanie pliku

with open('pan_tadeusz.txt', 'r', encoding='cp1252') as fopen:
  content = fopen.read()
print(content)