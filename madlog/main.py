import sys
import cx_Oracle
import os
from time import sleep
from tqdm import tqdm
import csv

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')  # dane do logowania
cursor = connection.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY:MM:DD:HH24:MI:SS'")


def create_resultfile(f_table_name, f_tabofvar, f_process_sample, f_ifns_info, f_ifns_info_steps):
    with open('file_data.txt', 'a') as f:
        if os.stat('file_data.txt').st_size == 0:
            print('table_name th_length th_last expected_val progress_cur progress_end', file=f)
            print('Utworzono nowy plik z danymi.')
        else:
            print('Znaleziono istniejacy plik z danymi.')

        th_last = str(f_tabofvar[-1][0])
        th_length = len(str(f_process_sample).split('.')[1])
        progress_cur = len(f_tabofvar)
        temp = (str(f_table_name) + " " + str(th_length) + " " + str(th_last) + " " + str(f_ifns_info) + " " + str(progress_cur) + " " + str(f_ifns_info_steps))
        f.write(temp+'\n')
        f.close()
        finito = (th_length, progress_cur)
        return finito


def dbmelt(db_table_name, db_ifns_info, db_machinfo_info, db_tabofvar, db_sample_info, db_process_info):
    global connection
    global cursor
    process_values = []
    tablecount = 0  # licznik tabel zgodnych z argumentem
    print(db_process_info)
    if db_sample_info[1] != db_ifns_info[0][2]:
        cursor.execute('select table_name from user_tables order by table_name')  # kursor
        for tablenames in cursor:  # petla ktora szuka zgodnych tabel
            if (db_table_name in tablenames) or (db_table_name.title() in tablenames):
                tablecount += 1  # inkrementacja licznika
        print("wololololo" + str(tablecount))
        if tablecount == 0:  # gdy nie istnieja tabele zgodne z plikiem w bazie danych
            temp = 'insert into madlog_db (PROCESSNAME, STARTINGVALUE, FINISHVALUE, NUMBEROFSTEPS, PC_NAME, PC_CORE) ' \
                   'values (:1, :2, :3, :4, :5, :6)'
            cursor.prepare(temp)
            temp = (db_table_name, float(db_ifns_info[0][0]), float(db_ifns_info[0][1]), float(db_ifns_info[0][2]), db_machinfo_info[0][0], float(db_machinfo_info[0][1]))
            process_values.append(temp)
            cursor.executemany(None, process_values)

            # cursor.execute(temp)
            temp = ('create table ' + db_table_name + ' (' + db_process_info[0][1] + ' number(9,3), SIGMA number(10,4), TIMESTAMP date)')
            cursor.execute(temp)

        temp = ('select max(' + db_process_info[0][1] + ') from ' + db_table_name)  # wyszukanie ostatniej wartosci
        print(temp)
        cursor.execute(temp)
        for db_temp in cursor:
            db_lastvalue = db_temp
        # print(type(db_lastvalue[0]))
        print('db_lastvalue ' + str(db_lastvalue[0]))
        if db_lastvalue[0] is None:  # gdy nie ma nic, to to sie ma wykonac
            temp = ("INSERT INTO "+db_table_name+" (" + db_process_info[0][1] +",SIGMA,TIMESTAMP) VALUES (:1, :2, :3)")
            cursor.prepare(temp)
            cursor.executemany(None, db_tabofvar)
        else:  # gdy zakonczono na jakiejs wartosci
            print(format(db_lastvalue[0], '.6g'))
            temp2 = None
            for pos, i in enumerate(db_tabofvar):
                var_temp = (format(i[0], '.3f'), format(i[1], '.3f'))
                if str(format(db_lastvalue[0], '.3f')) in var_temp:
                    print('success')
                    print(pos)
                    temp2 = pos+1
            if temp2 is None:
                print("Nie znaleziono wartości na której zakończono ostatni przebieg.")
                print("Czy wybrać ostatnią znaną wartośc zapisaną w pliku pomocniczym? (Y, N) "
                      "Ostatnia wartosc to: " + db_sample_info[1])
                decision = 'Nopo'
                while decision is not 'Y':
                    decision = input()
                    if (decision == 'Y') or (decision == 'y'):
                        temp2 = db_sample_info[1]
                    elif(decision == 'N') or (decision == 'n'):
                        temp2 = None
                    else:
                        print('Wybierz poprawna opcje - Y lub N')
                if temp2 is None:
                    print("Czy rozpoczac wysylanie danych do bazy od poczatku danych?")
                    decision = ' '
                    while decision is not 'Y':
                        decision = input()
                        if (decision == 'Y') or (decision == 'y'):
                            temp2 = 0
                        elif(decision == 'N') or (decision == 'n'):
                            temp2 = None
                        else:
                            print('Wybierz poprawna opcje - Y lub N')
            if temp2 is not None:
                for i in range(temp2, len(db_tabofvar)):

                    temp = ("INSERT INTO "+db_table_name+" (" + db_process_info[0][1] + ",SIGMA,TIMESTAMP) VALUES (:1, :2, :3)")
                    cursor.prepare(temp)
                    cursor.executemany(None, db_tabofvar)
    else:
        print("Plik nie wymaga dalszej analizy")


def getinfo(cur_file):
    lookup_sigma = 'sigma'  # deklaracja zmiennej, ktora wyszuka slowo sigma
    linenumb_sigma = -10
    lookup_ifns = '# i f ns'  # deklaracja zmiennej, ktora wyszuka ciag
    linenumb_ifns = -10
    lookup_machinfo = 'machine'
    linenumb_machinfo = -10
    tabofvar = []  # tablica, w ktorej beda przechowywane dane z pliku
    ifns_info = []
    machinfo_info = []
    process_info = []

    with open(cur_file, 'r', encoding='UTF-8') as myFile:
        for num, line in enumerate(myFile, 0):  # wyszukiwanie linii, od ktorych rozpoczynaja sie operacje
            # print line
            # print num
            if lookup_sigma in line:
                print('found sigma at line: '+ str(num) + str(line))
                linenumb_sigma = num
            if lookup_ifns in line:
                print('found ifns at line: ', num)
                linenumb_ifns = num
            if lookup_machinfo in line:
                print('found machine info at line: ', num)
                linenumb_machinfo = num
            if num == linenumb_sigma:
                process_info.append(line.split())
            if num == linenumb_ifns+1:
                ifns_info.append(line.split())
            if num == linenumb_machinfo+1:
                machinfo_info.append(line.split())
    print(ifns_info[0][0], ifns_info[0][1], ifns_info[0][2])
    print(machinfo_info[0][0], machinfo_info[0][1])

    with open(cur_file, 'r', encoding='UTF-8') as myFile:  # zastapic 'with open...'

        linenumb_sigma += 1

        lines = myFile.readlines()  # wczytywanie linii do bufora po kolei
        lines_len = len(lines)  # koncowa granica pliku
        lines_range = range(linenumb_sigma, lines_len)  # zakres na ktorym sczytywane sa dane

        lines = None  # czyszczenie bufora

        myFile.seek(0)  # przesuniecie wskaznika w pliku na poczatek

        i = 0
        j = 0
        readCSV = csv.reader(myFile, delimiter=' ')
        for row in readCSV:
            if i in lines_range:
                process = float(row[0])
                if (i == lines_range[0]+1) and (j == 0):
                    j += 1
                    process_sample = process
                sigma = float(row[1])
                date = row[2]
                temp = (process, sigma, date)
                tabofvar.append(temp)
            i += 1

    #myFile.close()
    table_name = cur_file.split('_')[0]
    sample_info = create_resultfile(table_name, tabofvar, process_sample, ifns_info[0][1], ifns_info[0][2])
    print(sample_info)
    # W TYM MIEJSCU MAJA WYKONYWAC SIE OPERACJE NA DB W OSOBNEJ FUKNCJI
    dbmelt(table_name, ifns_info, machinfo_info, tabofvar, sample_info, process_info)


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
    for fileinfo in tqdm(file_table):  # petla, ktora obrabia kazdy z tych plikow z osobna
        getinfo(fileinfo)
        sleep(2)
    connection.commit()

if __name__ == "__main__":
    main()
