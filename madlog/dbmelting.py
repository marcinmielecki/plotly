import cx_Oracle
import sys

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')  # dane do logowania
tablecursor = connection.cursor()


def dbmelt(a):
    table_name = "Wolollolo"  # tymczasowe gowno
    ifns_info = [[0 for x in range(3)] for x in range(3)]  # tymczasowe gowno
    ifns_info[0][0] = 666  # tymczasowe gowno
    ifns_info[0][1] = 766  # tymczasowe gowno
    ifns_info[0][2] = 866  # tymczasowe gowno
    machinfo_info = [[0 for x in range(5)] for x in range(5)]  # tymczasowe gowno
    machinfo_info[0][0] = "bestia"  # tymczasowe gowno
    machinfo_info[0][1] = 1000  # tymczasowe gowno
    exist_tables = []
    tablecount = 0  # licznik tabel zgodnych z argumentem
    tablecursor.execute('select table_name from user_tables order by table_name')  # kursor
    for tablenames in tablecursor:  # petla ktora szuka zgodnych tabel
        if a in tablenames[0]:
            # print(tablenames[0]) #wyswietlanie zgodnych wynikow
            exist_tables.append(tablenames[0])
            tablecount += 1  # inkrementacja licznika
    if tablecount == 0:  # gdy nie istnieja tabele zgodne z plikiem w bazie danych
        temp = ('insert into madlog_db (PROCESSNAME, STARTINGVALUE, FINISHVALUE, NUMBEROFSTEPS, PC_NAME, PC_CORE) '
                'values ('+str(table_name)+','+str(ifns_info[0][0])+','+str(ifns_info[0][1])+','+str(ifns_info[0][2])
                +','+str(machinfo_info[0][0])+','+str(machinfo_info[0][1])+')')
        print(temp)
        temp = ('create table ' +table_name+' (TH13 number(9,3), SIGMA number(10,4), TIMESTAMP date)')
        print(temp)
    else:  # gdy istnieja
        temp = ('select max(th13) from' +table_name)  # wyszukanie ostatniej wartosci
        print(temp)
        if temp is None:  # gdy nie ma nic to sie ma wykonac
            for i in range(len(tabofvar)):
                print('INSERT INTO', table_name, '(TH13,SIGMA,TIMESTAMP) VALUES (', tabofvar[i][0], ',', tabofvar[i][1], ',', tabofvar[i][2], ')')
                print('\n')
        else:  # gdy zakonczono na jakiejs wartosci
            temp2 = tabofvar.index(temp)
            for i in range(temp2, len(tabofvar)):
                print('INSERT INTO', table_name, '(TH13,SIGMA,TIMESTAMP) VALUES (', tabofvar[i][0], ',', tabofvar[i][1], ',', tabofvar[i][2], ')')
                print('\n')

test = 'T998'
dbmelt(test)
