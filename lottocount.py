# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:59:50 2017

@author: stu
"""
########################export into csvfile
import os
import cx_Oracle
import csv
 
SQL="SELECT * FROM lott"
 

filename=r"D:\data\lotto.csv"
FILE=open(filename,"w")
output=csv.writer(FILE, dialect='excel',delimiter=',', lineterminator='\n')
printHeader = True

 
connection = cx_Oracle.connect('scott/tiger@192.168.19.12:1522/orcl')
 
cursor = connection.cursor()
cursor.execute(SQL)
if printHeader:
    cols=[]
    for col in cursor.description:
        cols.append(col[0])
        
output.writerow(cols)    
for row in cursor:
    output.writerow(row)
   
cursor.close()
connection.close()
FILE.close()
#############################################


sum=0
import csv
lotto = csv.reader(open(r"D:\data\lotto.csv"))
for j in range(1,50,1):
    for i in lotto:
        if i[1]==str(j):
            sum += 1
    print(j,'count :  ',sum)   
    sum=0
    

sum=0
import csv
lotto = csv.reader(open(r"D:\data\lotto.csv"))
for i in lotto:
    if i[1]=='3':
        sum += 1
print(sum)   


for i in lotto:
   i[1]