# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:11:41 2017

@author: stu
"""


###########################################################
import cx_Oracle
import csv
 
SQL="SELECT * FROM dept" #CSV파일의 내용이 될 쿼리문
 

filename=r"D:\data\dept3.csv" #생성파일이 저장될 경로 및 파일명
FILE=open(filename,"w")
output=csv.writer(FILE, dialect='excel',delimiter=',', lineterminator='\n')
printHeader = False #헤더 생성 여부 True면 생성 / False면 생성하지 않음.

 
connection = cx_Oracle.connect('scott/tiger@192.168.19.12:1522/orcl') #오라클 계정
 
cursor = connection.cursor()
cursor.execute(SQL)
if printHeader: #헤더 생성
    cols=[]
    for col in cursor.description:
        cols.append(col[0])
    output.writerow(cols) 
        
   
for row in cursor:#행 생성
    output.writerow(row)
   
cursor.close()
connection.close()
FILE.close()

###########################################################

import pandas as pd
lotto = pd.read_csv(r"D:\data\lotto.csv")
sum=0
import csv
lotto = csv.reader(open(r"D:\data\lotto.csv"))
for i in lotto:
    if i[1]=='1':
        sum += 1
print(sum)      

import csv
file = open(r"D:\data\emp2_comm.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    print(i[5])