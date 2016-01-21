import os

temp = 'wyniki.txt'
f = open(temp, 'a')

if os.path.isfile(temp):
    print('Znaleziono plik')
    f.write('t666 0.7777 10/50\n')
    f.close()
else:
    print('tablename lastval progress', file=f)
    f.close()
    print('Utworzono')
