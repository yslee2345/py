# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:57:44 2017

@author: stu
"""

#문제1. 숫자를 물어보게하고 짝인지 홀인지

a=input('# : ')
if int(a)%2 ==1:
    print('홀수')
else:
    print('짝수')

#문제2. 홀짝임을 구분하는 mod함수를 생성하시오.
def mod(num):
    if int(num)%2==1:
        print('홀수')
    else:
        print('짝수')

mod(10)

#문제3. 이름을 물어보게 하고 이름을 입력하면 해당 사원이 고소득자인지 저소득자인지 출력
import csv
a=input('이름 : ')
emp_csv=csv.reader(open(r'D:\data\emp_comm.csv'))
for i in emp_csv:
    if i[1]==a:
        if int(i[5])>=3000:
            print('고소득자')
        elif int(i[5])>=2000:
            print('적당')
        elif int(i[5])<2000:
            print('저소득')

#문제4. 위 문제에서 이름을 소문자로 입력해도 되게끔.

import csv
a=input('이름 : ').upper()
emp_csv=csv.reader(open(r'D:\data\emp_comm.csv'))
for i in emp_csv:
    if i[1]==a:
        if int(i[5])>=3000:
            print('고소득자')
        elif int(i[5])>=2000:
            print('적당')
        elif int(i[5])<2000:
            print('저소득')
            
#문제5. (알고리즘 문제) 가우스 공식으로 1부터 10까지의 숫자의 합을 출력
a=int(input('# 1 : '))
b=int(input('# 2 : '))

c= (b*(b+1)/2) - (a*(a-1)/2)

print(c)
#문제6. 위의 문제를 다시 수행하는데 아래와 같이 큰 숫자를 먼저 입력하면 첫번째 입력한 숫자가 큽니다.
a=int(input('# 1 : '))
b=int(input('# 2 : '))
if a>b:
    print('#1 이 더 큼')
else:
    c= (b*(b+1)/2) - (a*(a-1)/2)  
    print(c)

#문제7. 구구단 2단 
for i in range(1,10):
    print(2,'*',i,'=',2*i);













