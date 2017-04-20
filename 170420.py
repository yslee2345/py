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


#문제8. 아래의 결과
#*
#**
#***
#****
a=int(input('#: '))
for i in range(1,a+1):
        print('*'*i)
    
#문제9 위와 반대로
a=int(input('#: '))
for i in range(a,0,-1):
        print('*'*i)
        
#문제10  마름모

        
#문제10 사각형
a=int(input('a : '))
b=int(input('b : '))

for i in range(1,b+1):
    for j in range(1,a+1):
        print('*',end='')
    print()
    
for i in range(b):
    result = ''.join('*' for i in range(a))
    print(result)

#join은 * 5개를 모아주는 메소드

#문제11 구구단을 가로로
for i in range(1,10):
    for j in range(2,10):
        print(j,'*',i,'=',i*j,end= ' ')
    print()

#문제12 for loop 이용하여 power 함수를 구현하시오.
a=int(input('밑수 : '))
b=int(input('지수 : '))
c=a

for i in range(1,b):
    a = a*c
    
print(a)

s='somestinrg'
numbers = sum(c.isdigit() for i in s)

words = sum( c.isalpha() for i in s)

spaces = sum(c.isspace() for i in s)
print(numbers)

#문제13. 겨울왕국 대본에는 숫자가 몇개 있는지

winter = open(r'D:\data\winter.txt','r')
lines = winter.readlines()
total = 0

for s in lines:
    total += sum(i.isdigit() for i in s)
    print(sum(i.isdigit() for i in s))

#문제14. 공백도아니고 알파벳도 아닌 숫자도 아닌 특수문자가 몇개
winter = open(r'D:\data\winter.txt','r')
lines = winter.readlines()
total = 0
total2 = 0

for s in lines:
    total2 += len(s)
    total += sum(i.isdigit() for i in s)+sum(i.isalpha() for i in s)+sum(i.isspace() for i in s)
print(total2-total)
    
#while문
print('몇번 반복할까요')
limit = int(input('반복할 횟수를 입력하세요~'))
count=0
while count < limit:
    count += 1
    print('{0}회 반복.'.format(count))

#문제 15. 숫자를 물어보게 하고 숫자를 입력하면 해당 숫자만큼 그림

a=int(input('# : '))
star =0
while star < a:
   star = star+1
   print((a-star)*' ',star*'*')
   
#문제16. 팩토리얼을 while loop
a = int(input('# : '))
cnt = 1
sum = 1
while a > 1:
    sum = sum*a
    a -= 1
print (sum)

#문제17. 로그함수를 파이선으로
a=float(input('밑수'))
b=float(input('진수'))
sum=0.00
while b/a>=1:
    b=b/a
    sum+=1
print(sum)

a=int(input('밑수를 입력하시오.'))
b=int(input('진수를 입력하시오.'))



#문제18. 두수를 입력받아 최대 공약수를 구하시오.
def gcd(bgr,sml):
    while bgr%sml>0:
        temp = sml
        sml = bgr%sml
        bgr = temp
    return sml
        
print(gcd(78696,19332))


#문제19. 최대공약수 알고싶은 2자 입력하세요.
a=input('2# : ')
b=[int(x) for x in a.split(' ')]
for i in b:
    b[i]=int(b[i])
bgr=b[0]
sml=b[1]

while bgr%sml>0:
    temp = sml
    sml = bgr%sml
    bgr = temp
print(sml)










