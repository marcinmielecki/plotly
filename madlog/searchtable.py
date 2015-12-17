import cx_Oracle
import sys

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')  #dane do logowania
tablecursor = connection.cursor()

#selected_table = None

def searchtable(a):
    exist_tables = []
    tablecount = 0 #licznik tabel zgodnych z argumentem
    tablecursor.execute('select table_name from user_tables order by table_name') #kursor
    for tablenames in tablecursor: #petla ktora szuka zgodnych tabel
        if a in tablenames[0]:
            #print(tablenames[0]) #wyswietlanie zgodnych wynikow
            exist_tables.append(tablenames[0])
            tablecount = tablecount + 1 #inkrementacja licznika
    if (tablecount == 0):
        print('Nie znaleziono bazy danych powiazanej z procesem '+ a +'. Czy utworzyc nowa? (Y/N)')
        decision = 'Chuj'
        while decision is not 'Y':
            decision = raw_input()
            if (decision == 'Y'):
                print('Stworzono')
                temp = "create table " +a+" (TH13 number(9,3), SIGMA number(10,4), TIMESTAMP date)"
                tablecursor.execute(temp)
                #selected_table = a
                return a
            elif(decision == 'N'):
                print('Nie stworzono')
                return 'Nie wybrano tabeli'
            else:
                print('Wybierz poprawna opcje - Y lub N')
    else:
        print('Znaleziono ponizsze bazy danych, ktora wybrac?')
        print(exist_tables)
        decision = None
        while decision not in exist_tables:
            decision = raw_input()
            if decision not in exist_tables:
                print('Zle wybrano, podaj ponownie')
            else:
                print('Wybrano tabele: '+decision)
                #selected_table = decision
                return decision

test = 'T999'
selected_db = searchtable(test)
print "Operacje beda wykonywane na tabeli "+selected_db
tablecursor.execute('commit')
