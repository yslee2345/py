# -*- coding: utf-8 -*-
"""

파이선의 내장함수와 사용자 정의 함수
Chapter1. Python's internal function & User defined function.
"""

#문제1 대문자 혹은 소문자로 출력하기
a='upper'
b='lower'

print(a.lower(),b.upper())

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1].lower(),emp_list[2].lower()) 
    
#문제2 이름을 출력하는데 이름의 첫번째 철자만 출력하고 소문자로 출력하시오

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1][0].lower())  
    
    

#문제3 이름을 출력하는데 이름의 두번째 철자부터 마지막까지 소문자로 출력하시오

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list.lower())  
    
    
#문제4. inicap함수를 정의하시오.
def init(inp):
   return inp[0].upper()+inp[1:].lower()
    
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (init(emp_list[1])) 
    
    """ 
    emp_list 자체는 타입이 list이기 때문에 전체는 안됨
    """

#문제5. 이름의 첫번째 철자부터 세번째 철자까지 출력되는 함수
def substr(string,fro,to):
    return string[fro-1:to]

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (substr(emp_list[1],1,3)) 

#문제6. 이름과 월급 출력하는데 월급을 출력할 때에 0 대신에 *을 출력하시오
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[5].replace('0','*')) 

    """
    CSV 파일은 문자로 가져온다 raw data가 숫자라고 한들.
    """

#문제7. 이름과 월급을 출력하는데 월급을 출력할 때에 0~2를 *로 출력

import csv
import re #정규식 모듈 import하고

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],re.sub('[0-2]','*',emp_list[5])) 
    
    """
    sub(pattern,repl,string)
    """


#문제8. 이름과 이름의 길이

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print (emp_list[1],len(emp_list[1]))  #연결연산자는 같은타입일때만 되는것을 잊지말자.

#문제9. 아래의 split함수의 예제를 수행해보시오

file = 'a b c d e f g'

print (len(file.split(' '))) #공백 하나를 분리해서 list 변수화 시킴.
      
#문제10. 아래의 file 변수 요소들을 list 변수에 담아서 두번째 요소를 출력하시오


file = 'a b c d e f g'

b=file.split(' ')

print(b[1]);


#문제11. 겨울왕국 대본을 공백을 구분으로 두고 나눠서 리스트 변수로 저장되게

file = open("D:\data\winter.txt",'r')
for winter_list in file:
    a = winter_list.split(' ')
    print (a)
    

#문제12. 위 스크립트 이용해서 겨울왕구 각 리스트 변수안에 단어가 몇개가 있는지 아래와 같이 출력되게.

file = open("D:\data\winter.txt",'r')
for winter_list in file:
    a = winter_list.split(' ')
    print(len(a))


#문제13. 겨울왕국에 단어수 구하기(중복포함)
file = open("D:\data\winter.txt",'r')
b=0
for winter_list in file:
    a = winter_list.split(' ')
    b +=len(a)
print(b)

#문제14. 겨울왕국 대본에는 Elsa가 몇번 나오는지 카운트 하시오!

#힌트
c=['Anna','Elsa','Anna','Elsa']
d=c.count('Elsa')
print(d)


file = open("D:\data\winter.txt",'r')
b=0
for winter_list in file:
    
    a = winter_list.split(' ')
    b+=a.count('Elsa')
    
print(b)

#문제15. emp.csv에서 14개의 리스트 변수중에 5번째 요소(월급) 부분만 담아서 리스트 변수로 아래와 같이 생성
a=[1,2,3]
a.append(4) #append는 리턴값이 없다. 리스트에 추가만 하는 것.
print(a) # a -> [1,2,3,4]

b=[]
b.append(1)
b.append(2)
b.append(3)
print(b) 
############################################################

import csv

b=[]
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    b.append(emp_list[5])
print(b)
    
#문제16. 겨울왕국 대본을 단어별로 출력하시오

file = open("D:\data\winter.txt",'r')
b=[]
for winter_list in file:
    
    a = winter_list.split(' ')
    for i in a:
        print(i)

#문제17. append 이용해서 하나의 list에 담으시오

file = open("D:\data\winter.txt",'r')
b=[]
for winter_list in file:
    
    a = winter_list.split(' ')
    for i in a:
        b.append(i)
print(b)


#문제18 위에서 \n제거하시오.
#strip함수
b=['not','yet\n','satisfied']
b.rstrip('\n')
print(b)

    #본 문제
file = open("D:\data\winter.txt",'r')
b=[]
for winter_list in file:
    
    a = winter_list.split(' ')
    for i in a:
        i=i.strip('\n')
        b.append(i)
print(b)

#문제19 rpad 함수를 생성하고 아래와 같이 실행되게
#
#rpad 구현

def rpad(string,space,string_2):
    if space-len(string)>=1:
        for i in range(space-len(string)):
            string=string+string_2
        return string
    else:
        return string[0:space]

#lpad 구현
def lpad(string,space,string_2):
    if space-len(string)>=1:
        for i in range(space-len(string)):
            string=string_2+string
        return string
    else:
        return string[0:space]

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
   print(rpad(emp_list[1],10,' '),lpad(emp_list[5],10,'*'))


#파이선 내장함수 (rpad,lpad)
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:

    print (emp_list[1].ljust(10), emp_list[5].rjust(10,'*') )


