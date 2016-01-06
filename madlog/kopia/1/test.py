temp = 'insert into madlog_db (PROCESSNAME, STARTINGVALUE, FINISHVALUE, NUMBEROFSTEPS, PC_NAME, PC_CORE) ' \
               'values (' + table_name + ',' + ifns_info[0][0] + ',' + ifns_info[0][1] + ',' + ifns_info[0][2] + ',' + \
               machinfo_info[0][0] + ',' + machinfo_info[0][1] + ')'
print(temp)
temp = "create table " + a + " (TH13 number(9,3), SIGMA number(10,4), TIMESTAMP date)"
print(temp)