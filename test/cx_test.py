import sys
import cx_Oracle

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')
cursor = connection.cursor()

print(connection.version)
print(connection.dsn)

cursor.execute('select * from testowa')
for result in cursor:
  print(result)
#cursor.close()
'''
j=(5,6,6,6,7)
k=(6,6,6,6,6)
n=len(j)
sql="insert into testowa (nazwa,n,k) values ('cx_oracle',:test,:test2)"

for i in range(0,n):
  cursor.execute(sql, test=j[i], test2=k[i])

cursor.execute('commit')'''
cursor.close()
connection.close()

