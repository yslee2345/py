# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:24:25 2017

@author: stu
파이선 변수와 for, if 문
"""
#문제1
a=1000
print(a)
print(type(a))

b='aaa'
print(b)
print(type(b))

#문제2
d=[1000,2000,3000,4000]
print(d)
print(type(d))

print(d[0])
print(d[1])

#문제3
for i in d:
    print(i)

for i in range(100):
    print(i)
    
#문제4
a=['7839','KING','PRESIDENT','0','1981-11-17','5000','','10']
print (a)
for i in a:
    print(i)
    
#문제5
a=['7839','KING','PRESIDENT','0','1981-11-17','5000','','10']

cnt = len(a)
print(cnt)

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list) 

#문제6
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],emp_list[5]) 
    
    
#문제7
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (len(emp_list))     
    

#문제8
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],len(emp_list[1])) 

#문제10
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[0],emp_list[1],emp_list[5])

#문제11
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],int(emp_list[5])*12)
    
#문제12

def ifnull(var1,var2):
    if var1 is '':
        return var2
    return var1

import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],ifnull(emp_list[6],0))


#문제13

def ifnull(var1,var2):
    if var1 is '':
        return var2
    return var1

import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],int(ifnull(emp_list[6],0))+int(emp_list[5]))




   