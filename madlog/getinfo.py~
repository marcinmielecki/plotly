import sys
import io
def getinfo():
    lookup_sigma = 'sigma'  # deklaracja zmiennej, ktora wyszuka slowo sigma
    linenumb_sigma = None
    lookup_ifns = '# i f ns'  # deklaracja zmiennej, ktora wyszuka ciag 
    linenumb_ifns = None
    tabofvar = []  # tablica, w ktorej beda przechowywane dane z pliku 

    with io.open('T654_pp_e-e-jj_th13_SR.txt', 'r', encoding='UTF-8') as myFile:
        for num, line in enumerate(myFile, 0):  # wyszukiwanie linii, od ktorych rozpoczynaja sie operacje
            print line
            if lookup_sigma in line:
                print('found sigma at line:', num)
                linenumb_sigma = line
            if lookup_ifns in line:
                print('found ite at line:', num)
                linenumb_ifns = line
    print(linenumb_sigma)
    print(linenumb_ifns)

getinfo()
