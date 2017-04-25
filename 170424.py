# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:46:17 2017

@author: stu
"""

#예제
import math
math.log(4,2)
math.log(10) # 밑수는 e이다.(자연로그)

def print_string(text,count=1): #count의 default 값은 1
    for i in range(count):
        print(text)
print(print_string("안녕하세요",2))

#문제1. 아래와 같이 이름만 넣으면 소속팀과 직위가 출력되는 함수
def print_inform(name,position='팀장',team='머신러닝'):
    print('이름 = {0}'.format(name))
    print('소속팀 = {0}'.format(team))
    print('직위 = {0}'.format(position))
    return 
    
print(print_inform('장경원'))

#예제(가변매개변수)
def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s + ' '
        
    return result
    print(text_list)

print(merge_string('아버지가','방에','들어','가신다.'))


#문제2. MIT TTT코드에서 보드판을 출력하는 printboard함수를 분석

EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [' ', 'X', 'O']
def printboard(state):
    """ Print the board from the internal state."""
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(*cells)
    print(BOARD_FORMAT.format(*cells))

printboard([[1,2,0],[0,2,0],[0,2,0]])
print(BOARD_FORMAT.format('a','b','c','d','e','f','g','h','g')) 
print(BOARD_FORMAT.format('x','o','x','o','x',' ',' ',' ',' '))
print(BOARD_FORMAT.format('x'.center(6),'o'.center(6),'x'.center(6),'o'.center(6),'x',' ',' ',' ',' '))

#예제)
def stop_fun(num):
    for i in range(1,num+1):
        print('숫자 {0}출력'.format(i))
        if i==5:
            return #10까지 돌아야 하지만 5에서 멈춘다. 즉, 함수를 종료하겠다 라는 의미와 같다.
print(stop_fun(10)) 
    
def enumstates(state, idx, agent):
    if idx > 8:
        player = last_to_act(state)
        if player == agent.player:
            agent.add(state)
    else:
        winner = gameover(state)
        if winner != EMPTY:
            return
        i = int(idx / 3)
        j = idx % 3
        for val in range(3):
              
               state[i][j] = val
               enumstates(state, idx+1, agent)
               
#문제3. 아래와 같이 숫자를 입력하고 함수를 실행하면 숫자가 세로로 출력되게 하시오.
def print_something(*val):
    for s in val:
        print(s)
      
    
print(print_something(1,2,3,4,5,6,7,8,9,10))



#예제
def scope_test():
    
    a=1
    print('a:{0}'.format(a))
    
scope_test()
a=0
scope_test()


#문제4. 위의 스크립트에서 마지막 scope_test()를 실행했을때 a가 1이 아니라 0이 출력되려면 함수를 생성할때 어떻게?
def scope_test():
    
    a=1
    print('a:{0}'.format(a))

scope_test()

print(a)

#예제 재귀 알고리즘의 예
def some_func(count):
    if count>0:
        some_func(count-1)
    print(count)
    
some_func(10)

#문제5. 10 factorial 을 재귀함수로 구현하여 출력하시오.
def rec_fact(count):    
    if count>0:             
        return count * rec_fact(count-1)    
    elif count==0:
        return 1

rec_fact(10)

#문제6. 최대공약수 (16,20) 재귀함수로 출력
def gcd(num1,num2):
    if num2==0:
        return num1
    return gcd(num2,num1%num2)


gcd(20,30)

#문제7. 가변 매개변수와 재귀 알고리즘을 이용해서 최대 공약수를 출력하는 함수를 생성


def gcd(*num):
    return num
  
print(gcd(10,20,30,40,50))

gcd(20,30)

#문제8. 3개 최대공약수
def gcd(num1,num2,num3):
    if num2==0:
        if num3==0:
            return num1
        return gcd(num3,num2,num1%num3)
    return gcd(num2,num1%num2,num3)

gcd(20,30,4)

#################개인공부################
#객체 지향
class Rectangle(object):
    
    def __init__(self, h,v):
        self.h=h
        self.v=v
        
    def area(self):
        return self.h * self.v

r=Rectangle(10,20)
a=r.area()
print(a)

#예제 1. 
class Triangle(object):
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def area(self):
        return self.r*self.h/2
    
r=Triangle(10,20)
a=r.area()
print(a)
    
#예제2.
class Calvol(object):
    def __init__(self, a,b,h):
        self.a=a
        self.b=b
        self.h=h
    def volume(self):
        return self.a*self.b*self.h
    def surface(self):
        return (self.a+self.b)*2*self.h + (self.a*self.b) *2
    
r=Calvol(10,10,20)
a1=r.volume()
a2=r.surface()
print(a1,a2)
        
class Character(object):
    def __init__(self):
        self.life=1000
        
    def attacked(self):
        self.life -= 10
        print(u"공격받음 : 생명력 =",self.life)
        
    def attack(self):
        print(u"공격 ! ")
        
a=Character()
b=Character()
c=Character()

print(a.life,b.life,c.life)

a.attacked()
a.attacked()
a.attacked()
a.attacked()
a.attacked()

class Warrior(Character):
    def __init__(self):
        super(Warrior,self).__init__()
        self.strength=15
        self.intelligence=5
        
    def attack(self):
        print(u"육탄공격! ")
    def attacked(self):
        self.life-=10

class Wizard(Character):
    def __init__(self):
        super(Wizard,self).__init__()
        self.strength=5
        self.intelligence=15
        
    def attack(self):
        print("마법공격 ! ")
        
    def attacked(self):
        self.life-=30

a=Wizard()
b=Warrior()

print(a.life,b.life)
print(a.strength,b.strength,a.intelligence,b.intelligence)
a.attack()
b.attack()
a.attacked()
b.attacked()
print(a.life,b.life)



            
            