import sys
import cx_Oracle
import os

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')  # dane do logowania
cursor = connection.cursor()

t_test = open("t654goly.txt","r")
tabofvar = []
for line in t_test:
    tabofvar.append(tuple(line.split()))
    print line

print tabofvar
'''
j = 0
for i in tabofvar:
    print(tabofvar[j])
    j += 1'''

reader = open("job_history.txt","r")
lines = []
for line in reader:
    lines.append(line)
    #print line
print lines

cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY:MM:DD:HH24:MI:SS'")
cursor.prepare("INSERT INTO T654 VALUES(:1,:2,:3)")
cursor.executemany(None, tabofvar)
connection.commit()
