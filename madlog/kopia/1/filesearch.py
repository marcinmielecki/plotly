import sys
import cx_Oracle
import os


def getinfo(cur_file):
    lookup_sigma = 'sigma'  # deklaracja zmiennej, ktora wyszuka slowo sigma
    linenumb_sigma = None
    lookup_ifns = '# i f ns'  # deklaracja zmiennej, ktora wyszuka ciag
    linenumb_ifns = -10
    lookup_machinfo = 'machine'
    linenumb_machinfo = -10
    tabofvar = []  # tablica, w ktorej beda przechowywane dane z pliku
    ifns_info = []
    machinfo_info = []

    with open(cur_file, 'r', encoding='UTF-8') as myFile:
        for num, line in enumerate(myFile, 0):  # wyszukiwanie linii, od ktorych rozpoczynaja sie operacje
            # print line
            # print num
            if lookup_sigma in line:
                print('found sigma at line: ', num)
                linenumb_sigma = num
            if lookup_ifns in line:
                print('found ifns at line: ', num)
                linenumb_ifns = num
            if lookup_machinfo in line:
                print('found machine info at line: ', num)
                linenumb_machinfo = num
            if num == linenumb_ifns+1:
                ifns_info.append(line.split())
            if num == linenumb_machinfo+1:
                machinfo_info.append(line.split())
    print(ifns_info[0][0], ifns_info[0][1], ifns_info[0][2])
    print(machinfo_info[0][0], machinfo_info[0][1])
    myFile = open(cur_file, 'r', encoding='UTF-8')

    linenumb_sigma += 1

    lines = myFile.readlines()  # wczytywanie linii do bufora po kolei
    lines_len = len(lines)  # koncowa granica pliku
    lines_range = range(linenumb_sigma, lines_len)  # zakres na ktorym sczytywane sa dane

    lines = None  # czyszczenie bufora

    myFile.seek(0)  # przesuniecie wskaznika w pliku na poczatek

    i = 0
    for line in myFile:  # funkcja przypisujaca zmienne do tablicy [# th13 sigma timestamp]
        if i in lines_range:  # warunek, ktory sprawdza czy jestesmy w zakresie
            # print(line.split())
            tabofvar.append(line.split())
        i += 1

    myFile.close()
    table_name = cur_file.split('_')[0]
    # W TYM MIEJSCU MAJA WYKONYWAC SIE OPERACJE NA DB W OSOBNEJ FUKNCJI
    print(table_name)
    print('insert into madlog_db (PROCESSNAME, STARTINGVALUE, FINISHVALUE, NUMBEROFSTEPS, PC_NAME, PC_CORE) values ('
          , table_name, ',', ifns_info[0][0], ',', ifns_info[0][1], ',', ifns_info[0][2], ',', machinfo_info[0][0], ',',
          machinfo_info[0][1], ')')
    for i in range(len(tabofvar)):
        print('INSERT INTO', table_name, '(TH13,SIGMA,TIMESTAMP) VALUES (', tabofvar[i][0], ',', tabofvar[i][1], ',', tabofvar[i][2], ')')
        print('\n')


def filesearch():
    foundfiles = []  # tablica, ktora bedzie przechowywac nazwy znalezionych plikow
    print("Prosze podawac sciezki uzywajac '//' oraz konczac tym samym symbolem, np. C://Windows// lub //home//.")

    folder_check = False
    while folder_check is False:
        folder_path = input("Podaj sciezke folderu z plikami: ")
        folder_check = os.path.isdir(folder_path)

    if folder_check is True:
        print("Folder znaleziono")
        print("Znaleziono nastepujace pliki w wybranym folderze: ")
        for file in os.listdir(folder_path):
            if file.endswith(".txt") and (file.startswith('T') or file.startswith('t')):  # szuka plikow na T lub t
                foundfiles.append(file)
                print(file)
        return foundfiles
    else:
        print("Folder nie istnieje, podaj poprawna sciezke.")


def main():
    file_table = filesearch()  # wywolanie funkcji wyszukujacej pliki w folderze
    print(file_table)
    for fileinfo in file_table:  # petla, ktora obrabia kazdy z tych plikow z osobna
        getinfo(fileinfo)

if __name__ == "__main__":
    main()


