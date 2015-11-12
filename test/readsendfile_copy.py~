import sys
#import cx_Oracle

print('\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n')

lookup = 'sigma'
linenumb = None
tablicatest = []

with open('T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8') as myFile:
  for num, line in enumerate(myFile, 0):
    if lookup in line:
      print('found at line:', num)
      linenumb=int(num)+1

myFile.close()

print(linenumb)

myFile = open('T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8')

lines=myFile.readlines()
lines_len=len(lines)

for i in range(linenumb,lines_len):
  print(lines[i].split())

myFile.close()

print('\n**************************** \n')

myFile = open('T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8')

linelist=range(linenumb,lines_len)
i=0
for line in myFile:
  if i in linelist:
    print(line.split())
    tablicatest.append(line.split())
  i=i+1
print('\n**************************** \n')
print(tablicatest[0][0])
print('\n**************************** \n')

"""

with open('T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8') as testopen:
  for line in testopen:
    for part in line.split():
      if "sigma" in part:
        print(part)

file_T = open('T439_e-e-_w2-w2-_th13_SR.txt','r',encoding='UTF-8')
for i in range(linenumb,15):
  print (file_T.readline())

print('****************************** \n')

for line in file_T:
  print(line)

print('############################## \n')

for i, line in enumerate(file_T):
  if x == 5:
    print(line)

file_T.close() """


