# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:46:28 2017

@author: stu
"""

#문제1. instr함수를 파이선으로 구현하시오.
def instr(string,target_string):
    for i in range(len(string)):
        if string[i]==target_string:
            return i+1
    return 0

print(instr('smith','i'))


#문제2. 이름, 이름에 M자가 몇번째 자리에 있는지.
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],instr(emp_list[1],'M'))

#문제3. (숫자함수)이름,월급,보너스 출력하는데 보너스는 월급의 15%로 출력하시오
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    bns=int(emp_list[5])*0.15
    print(emp_list[1],emp_list[5],round(bns,-1))
      
#문제4. 위의 결과에서 컬럼명도 출력되게.      

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
print('ename'.ljust(10),'sal'.ljust(10),'bonus')
print('-------------------------------')
for emp_list in emp_csv:
    bns=int(emp_list[5])*0.15
    print(emp_list[1].ljust(10),emp_list[5].ljust(10),bns)
      
#문제5. 위에서 반올림 되게 하시오.
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
print('ename'.ljust(10),'sal'.ljust(10),'bonus')
print('-------------------------------')
for emp_list in emp_csv:
    bns=int(emp_list[5])*0.15
    print(emp_list[1].ljust(10),emp_list[5].ljust(10),round(bns))
            
#문제6. 보너스를 출력할 때 소수점 이하를 trunc를 사용해서 잘라내시오

import csv,math

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
print('ename'.ljust(10),'sal'.ljust(10),'bonus')
print('-------------------------------')
for emp_list in emp_csv:
    bns=int(emp_list[5])*0.15
    print(emp_list[1].ljust(10),emp_list[5].ljust(10),math.trunc(bns))


#문제7. input 명령어를 이용해서 숫자를 입력받아 해당 숫자가 짝수인지 홀수인지 출력되게.
def odd_even(num):
    num=int(num)
    if num%2==1:
        return 'Odd Number'
    else:
        return 'Even Number'

num=input('#1 : ')


print(odd_even(num))

#문제8. (power함수) power함수를 이용해서 아래의 프로그램 구현.
#숫자를 입력하세요. / 지수를 입력하세요 

a = int(input('#밑수 : '))
b = int(input('#지수 : '))

print(pow(a,b))


#문제9. 오늘 날짜를 출력.
import datetime

print(datetime.date.today())
#or
from datetime import date
print(date.today())


#문제10. 오늘부터 3달 뒤의 날짜를 출력하시오
from datetime import date
from dateutil.relativedelta import relativedelta

result=date.today() + relativedelta(months=+3)
print(date.today())
print(result)

#문제11. 이름,입사일,입사한 날짜에서 3달후의 날짜를 출력하시오.
import csv
import datetime
from dateutil.relativedelta import relativedelta

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    result=datetime.datetime.strptime(emp_list[4],'%Y-%m-%d')+ relativedelta(months=+3)
    print(emp_list[1],emp_list[4],result)

#문제12. 올해 2월달의 마지막 날짜를 출력하시오
from calendar import monthrange
import datetime
print(monthrange(2017,2))

#문제13. 오늘부터 이번달 말일까지 총 며칠남았는지?
from calendar import monthrange
import datetime
print(datetime.date.today())
print (monthrange(2017,5)[1])
a= monthrange(2017,4)[1]-datetime.date.today().day
print (a)
#monthrange는 튜플형태로 반환한다. [1]은 해당 달이 총 며칠인지 리턴한다.

#문제14. 오늘이 무슨 요일인지 출력하시오.
import datetime

def weekday(str1):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    str1 = datetime.datetime.strptime(str1,'%Y/%m/%d').weekday()
    return days[str1]

date=datetime.date.today()
print(weekday(date))
print(datetime.date.today())
#print(weekday('1991-12-08'))

#문제14. 이름, 입사한 요일
def weekday(str1):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    str1 = datetime.datetime.strptime(str1,'%Y-%m-%d').weekday()
    return days[str1]

import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[4],weekday(emp_list[4]))
    
#문제15. 오늘날짜에서 하루를 더한 날짜가 어떻게?
import datetime
print(date.today()+datetime.timedelta(days=1))

#문제16. 아래와 같이 실행되는 사용자 정의 함수를 생성하시오.
def next_day(str1):
    str1 = datetime.datetime.strptime(str1,'%Y-%m-%d')
    return str1+datetime.timedelta(days=1)

print(next_day('2017-04-17'))

#문제17 next_day 함수구현
def next_day(str1,weekday):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for i in range(len(days)):
        if days[i]==weekday:
            j=i
    str1 = datetime.datetime.strptime(str1,'%Y-%m-%d')
    str2=str1
    str1 = str1.weekday()
    if str1==j:
        return str2+datetime.timedelta(days=7)
    else:
        return str2+datetime.timedelta(days=abs(str1-j))  

print(next_day('2017-04-17','Sunday'))        
                
#문제18. 이름, 입사한 날짜부터 오늘까지 총 며칠 근무했는지 출력하시오

import datetime
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv: 
    retun = date.today()-datetime.datetime.strptime(emp_list[4],'%Y-%m-%d').date()
    print(emp_list[1],emp_list[4],retun)

print(date.today())
print(datetime.datetime.strptime('1991-12-08','%Y-%m-%d'))

#문제19. (input명령어와 if문을 이용한 문제) if문을 사용해서 사원번호가 7788번인 사원의 사원이름과 월급을 출력하시오.
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv: 
    if emp_list[0]=='7788':
        print(emp_list[2],emp_list[5])

#문제20 월급이 3000이상인 사원들의 이름과 월급
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if int(i[5])>=3000:
        print(i[2],i[5])

#문제21. 1981/11/17에 입사한 사원들의 이름과 입사일을 출력하시오
import csv
import datetime

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if datetime.datetime.strptime(i[4],'%Y-%m-%d') == datetime.datetime.strptime('1981-11-17','%Y-%m-%d'):
        print(i[1],i[4])
###변환하지 않아도 됨.

#문제22. (틱택토 프로그램 이해) 81년도에 입사한 사원들의 이름과 입사일
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if i[4][0:4] in '1981':
        print(i[1],i[4])
   
#문제23. 아래의 리스트 변수 중 positive 라는 단어는 몇개가 나오는가?

word=['winter','cold','positive','negative']
sum=0
for i in word:
    if 'positive'==i:
        sum = sum+1
print (sum)

#문제24. 아래의 리스트 변수 중 positive, negetive 라는 단어는 몇개가 나오는가?
word=['winter','cold','positive','positive']
sum=0
for i in word:
    if i in ['positive','negative']:
        sum = sum+1
print (sum)

#문제25. 겨울왕국 대본에는 긍정적인 단어가 몇개나 들어있는가?

file = open("D:\data\positive-words2.txt",'r')
positive=[]
for i in file:
    a = i.split(' ')
    for j in a:   
        j=j.strip('\n')
        positive.append(j.lower())

file = open("D:\data\winter.txt",'r')
b=[]
for winter_list in file:
    
    a = winter_list.split(' ')
    for i in a:
        i=i.strip('\n')
        i=i.strip('"')      
        i=i.strip('.')
        i=i.strip(',')
        i=i.strip('!')
        i=i.strip('?')
        i=i.strip(':')
        i=i.strip('(')
        i=i.strip(')')
     
        b.append(i.lower())


sum=0
for i in b:
    if i in positive:
        sum+=1;
print(sum)


file = open(r"D:\data\negative-words.txt",'r')
positive=[]
for i in file:
    a = i.split(' ')
    

import re
positive = []
sum = 0

for i in open("D:\data\positive-words2.txt",'r'):                                     
    print(i)
    #positive.append((re.sub("\n",'',i)).upper())

for j in open("D:\data\winter.txt",'r'):                                                      
    for k in re.sub('[^A-z ]','',re.sub('\n','',j)).upper().split(' ') :    
        if k == positive:                                                                                         
            sum = sum +1 
print(sum)


for j in open("D:\data\winter.txt",'r'):
    
    for k in re.sub('[^A-z ]','',re.sub('\n','',j)).upper().split(' '):
        print(k)

for j in open("D:\data\winter.txt",'r'):
    print(j)
