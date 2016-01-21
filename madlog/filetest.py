import os

temp = 'wyniki.txt'
with open(temp, 'a') as f:
    if os.stat(temp).st_size == 0:
        print('tablename lastval progress', file=f)
        f.close()
        print('Utworzono')
    else:
        print('Znaleziono plik')
        f.write('t666 0.7777 10/50\n')
        f.close()


def testo():
    plik = 'C:\\Users\\Kamil\\Desktop\\docs\\python_projekt\\file_data.txt'
    f = open(plik)
    output = []
    for line in f:
        if (temp in line.strip()) or (temp.title() in line.strip()):
            print(line.strip())
            print('wololo')
            output.append('wololo\n')
        else:
            output.append(line)
    f.close()
    f = open(plik, 'w')
    f.writelines(output)
    f.close()
