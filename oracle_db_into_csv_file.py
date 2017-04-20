# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:11:41 2017

@author: stu
"""



import os
import cx_Oracle
import csv
 
SQL="SELECT * FROM lott"
 

filename=r"D:\data\lotto.csv"
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')
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
    output.writerow()
   
cursor.close()
connection.close()
FILE.close()

import pandas as pd
lotto = pd.read_csv(r"D:\data\lotto.csv")

import csv
lotto = csv.reader(open(r"D:\data\lotto.csv"))
for i in lotto:
   print(i)
    

import csv
file = open(r"D:\data\emp2_comm.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    print(i[5])