# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:56:16 2017

@author: stu
"""

#재귀알고리즘 복습
def gcd(num1,num2):
    if num2==0:
        return num1
    else:
        gcd(num2,num1%num2)
    return num1

def fact(num):
    if num==0:
        return 1
    else:
       return num*fact(num-1)

fact(10)

#표준편차를 구하기 위한 함수
import math

def stddev(*args):
    
    def mean():
        return sum(args)/len(args)
    
    def variance(m):
        total = 0
        for arg in args:
            total += (arg-m)**2
        return total/(len(args)-1)
    
    v=variance(mean())
    return math.sqrt(v)

print(stddev(2.3,1.7,1.4,0.7,1.9))

#클래스로 전환

class Stddev(object):
    
    def __init__(self,*args):
        self.*args = *args
        
    def mean():
        return sum(args)/len(args)
    def variance(m):
        total =0
        for arg in args:
            total += (arg-m)**2
        return total/(len(args)-1)
    
    def result():
        v=variance(mean())
        return math.sqrt(v)

#문제1. 가변 매개변수 이용하여 최대 공약수를 출력하는 중첩 함수를 생성하시오.

def gcd(*args):
                                                                
    def gcd_2(a):                         
        b=gcd_3(max(a),min(a))                                                 
        a.remove(min(a))                
        a.remove(max(a))                                                        
        a.append(b)                     
        if max(a)==min(a):              
            a[0]
        else:
            gcd_2(a)
        
    def gcd_3(a,b):                                                            
        if min(a,b) == 0:               
            return max(a,b)             
        return gcd_3(b,a%b)
    
    a = []                         
    for i in args:             
        a.append(i)
    gcd_2(a) 
    return a[0]
print(gcd(25,10))


gcd(40,20,30,40)    
    
#문제2. 탐욕 알고리즘을 이용하여 지불해야 하는 금액을 가장 적은 수의 화폐로 지불하시오.(1원 50원 100원 / 362)
def greedy(num):
    cash=[100,50,1]
    j=[]
    for i in cash:
       res = divmod(num,i)
       num = res[1]      
       j.append(res[0])
    return j
        
print(greedy(400))

#문제3. 위 알고리즘을 재귀 알고리즘을 사용하여.
import math

def greedy(num):  
    if num>=100:  
        global p
        p=[]
        j=math.trunc(num/100)
        p.append(j)
        num=num % 100
        return greedy(num)    
    elif num>=50:        
        j=math.trunc(num/50)
        p.append(j)
        num=num % 50        
        return greedy(num)
    elif num<50:
        p.append(int(num/1))
        num==0        
        return p
 
print(greedy(362))
    
#다른방법

def coinGreedy(money, cash_type):
    def coinGreedyRecursive(money, cash_type, res, idx):
        if idx >= len(cash_type): #화폐 다 사용 시 종료
            return res
        dvmd = divmod(money,cash_type[idx])
        res[cash_type[idx]]=dvmd[0]
        return coinGreedyRecursive(dvmd[1],cash_type,res,idx+1)
        
    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬
    return coinGreedyRecursive(money,cash_type,{},0)
money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for key in res:
    print('{0}원 : {1}개'.format(key,res[key]))


#예제. 모듈 생성 예

print(divide(2,3))

#문제4. 오전에 만들었던 최대공약수 구하는 함수를 모듈화 하시오
import gcd

print(gcd.gcd(10,20,30,40))

#문제5. 표준편차를 출력하는 함수를 모듈화시켜 다른 실행창에서 아래와 같이 실행하면 실행되게 하시오.
import std

print(std.stddev(2.3,1.7,1.4,0.7,1.9))

#예제. sys 모듈
import sys
print(sys.builtin_module_names)

import sys
for path in sys.path:
    print(path)
    
#문제6. sys 모듈의 random 함수를 이용하여 원주율 구하는 코드를 실행해보시오.




