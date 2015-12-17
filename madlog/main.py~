import sys
import cx_Oracle
import os


def filesearch():
    print("Prosze podawac sciezki uzywajac '//' oraz konczac tym samym symbolem, np. C://Windows// lub //home//.")

    folder_check = False
    while(folder_check == False):
        folder_path = input("Podaj sciezke folderu z plikami: ")
        folder_check = os.path.isdir(folder_path)

    if(folder_check == True):
        print("Folder znaleziono")
        print("Znaleziono nastepujace pliki w wybranym folderze: ")
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                print(file)
        file_check = False
        while(file_check == False):
            file_path = input("Wybierz plik, ktory chcesz obrobic: ")
            file_check=os.path.exists(folder_path+file_path)
            if(file_check == True):
                print("Wybrany plik jest poprawny")
                break
            else:
                print("Wybrano niepoprawny, lub nieisteniejacy plik")
    else:
        print("Folder nie istnieje, podaj poprawna sciezke.")
    filefolder_path = (folder_path+file_path)
    print("Wybrany plik to: "+filefolder_path)


lookup_sigma = 'sigma'  # deklaracja zmiennej, ktora wyszuka slowo sigma
linenumb_sigma = None
lookup_ite = '# i f ns'  # deklaracja zmiennej, ktora wyszuka slowo ite
linenumb_ite = None
tabofvar = []  # tablica, w ktorej beda przechowywane dane z pliku

with open('T654_pp_e-e-jj_th13_SR.txt', 'r', encoding='UTF-8') as myFile:
    for num, line in enumerate(myFile, 0):  # wyszukiwanie linii, od ktorych rozpoczynaja sie operacje
        if lookup_sigma in line:
            print('found sigma at line:', num)
            linenumb_sigma = int(num)+1
        if lookup_ite in line:
            print('found ite at line:', num)
            linenumb_ite = int(num)+1

myFile = open('T654_pp_e-e-jj_th13_SR.txt', 'r', encoding='UTF-8')

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
    i = i+1

myFile.close()

for i in range(len(tabofvar)):
    print('INSERT INTO RT_TEST (test1,test2,test3) VALUES (', tabofvar[i][0], ',', tabofvar[i][1], ',', tabofvar[i][2], ')')
    print('\n')

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')  # dane do logowania
cursor = connection.cursor()

print("Polaczono z baza danych w wersji:", connection.version)

cursor.execute('select * from testowa')
for result in cursor:
    print(result)
# cursor.close()

cursor.execute('select th13 from t654 where th13 in (select max(th13) from t654)')
for testo in cursor:
    print("Sczytano wartosc")
print("Ostatnia wartosc z tabeli to:", testo[0])

some_var = 'aaabbbccc'[:5]
print(some_var)

j = (5, 6, 6, 6, 7)
k = (6, 6, 6, 6, 6)
n = len(j)
plik = "testowa"
sql = ("insert into "+plik+" (nazwa,n,k) values ('cx_oracle',:test,:test2)")

print(sql)
'''for i in range(0,n):
  cursor.execute(sql, test=j[i], test2=k[i])

cursor.execute('commit')'''
cursor.close()
connection.close()

filesearch()
