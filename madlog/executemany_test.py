import sys
#import cx_Oracle
import os
import io
from time import sleep

lookup_sigma = 'sigma'  # deklaracja zmiennej, ktora wyszuka slowo sigma
linenumb_sigma = None
lookup_ifns = '# i f ns'  # deklaracja zmiennej, ktora wyszuka ciag
linenumb_ifns = -10
lookup_machinfo = 'machine'
linenumb_machinfo = -10
tabofvar = []  # tablica, w ktorej beda przechowywane dane z pliku
ifns_info = []
machinfo_info = []
with open('/home/student/Dokumenty/infpro-9/madlog/T654_pp_e-e-jj_th13_SR.txt', 'r', encoding='UTF-8') as myFile:
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
myFile = open('/home/student/Dokumenty/infpro-9/madlog/T654_pp_e-e-jj_th13_SR.txt', 'r', encoding='UTF-8')

linenumb_sigma += 1

lines = myFile.readlines()  # wczytywanie linii do bufora po kolei
lines_len = len(lines)  # koncowa granica pliku
lines_range = range(linenumb_sigma, lines_len)  # zakres na ktorym sczytywane sa dane

lines = None  # czyszczenie bufora

myFile.seek(0)  # przesuniecie wskaznika w pliku na poczatek

i = 0
for line in myFile:  # funkcja przypisujaca zmienne do tablicy [# th13 sigma timestamp]
    if i in lines_range:  # warunek, ktory sprawdza czy jestesmy w zakresie
        print(tuple(line.split()))
        tabofvar.append(tuple(line.split()))
    i += 1
print(tabofvar[0])

