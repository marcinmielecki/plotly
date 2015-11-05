import cx_Oracle

file_T = open('C:/Users/Kamil/Documents/GitHub/infpro-9/T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8')
for i in range(0,10):
    print (file_T.readline())

print('############################## \n')

for line in file_T:
    print(line)

