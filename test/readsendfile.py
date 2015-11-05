import sys
import cx_Oracle

with open('C:/Users/Kamil/Documents/GitHub/infpro-9/T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8') as testopen:
    for line in testopen:
        for part in line.split():
            if "sigma" in part:
                print(part)

print('\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n')

lookup = 'sigma'

with open('C:/Users/Kamil/Documents/GitHub/infpro-9/T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8') as myFile:
    for num, line in enumerate(myFile, 0):
        if lookup in line:
            print('found at line:', num)

print('\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n')


file_T = open('C:/Users/Kamil/Documents/GitHub/infpro-9/T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8')
for i in range(0,10):
    print (file_T.readline())

print('############################## \n')

for line in file_T:
    print(line)

print('############################## \n')

for i, line in enumerate(file_T):
    if x == 5:
        print(line)

file_T.close()


