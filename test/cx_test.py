import sys
import cx_Oracle

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')
cursor = connection.cursor()

print(connection.version)
print(connection.dsn)

cursor.execute('select * from newton')
for result in cursor:
    print(result)
cursor.close()
connection.close()

