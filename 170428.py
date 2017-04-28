#문제1. gun 인스턴스 생성 위한 gun()클래스 생성
class Gun():
    def __init__(self):
        self.bullet = 0

    def charge(self,num):
        self.bullet = num

    def shoot(self,num):
        for i in range(num):

            if self.bullet>0:
                print('탕!')
                self.bullet -= 1

            elif self.bullet==0:
                print('장전하세요')
                break

    def print(self):
        print('총알이 {0}발 남았습니다.'.format(self.bullet))

gun1=Gun()
gun1.charge(10)
gun1.shoot(3)
gun1.print()

gun2=Gun()
gun2.charge(10)
gun2.shoot(6)
gun2.print()
#위 2개의 총은 서로 별개의 총이다. 같은 설계도를 사용했지만. 별개의 총이 맞는지 확인해본다.
print(gun1)
print(gun2)
#같은 설계도인지?
print(gun1.__class__)
print(gun2.__class__)

#예제 딕셔너리와 클래스
student = {'name':'김인호','year':2,'class':3,'student_id':35}
print('{},{}학년 {}반 {}번'.format(student['name'],student['year'],student['class'],student['student_id']))

class Student(object):
    def __init__(self,name,year,class_num,student_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id

    def introduce_myself(self):
        return '{}, {}학년 {}반 {}번'.format(self.name,self.year,self.class_num,self.student_id)

student = Student('김인호',2,3,35)
student2 = Student('김김김',3,4,5)
print(student2.introduce_myself())

#문제2. 위 코드에서 self를 빼면?
class Student(object):
    def __init__(self,name,year,class_num,student_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id

    def introduce_myself(self):
        return '{}, {}학년 {}반 {}번'.format(self.name,self.year,self.class_num,self.student_id)

student = Student('김인호',2,3,35)
student2 = Student('김김김',3,4,5)
print(student2.introduce_myself())

#문제3. 자기자신이 인스턴스의 메소드에 인자로 전달된다는 것이 어떤 것인지 인스턴스를 통하지 않고 바로 introduce_myself직접 호출해서  확인
class Student(object):

    def __init__(self,name,year,class_num,student_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id

    def introduce_myself(self):
        return '{}, {}학년 {}반 {}번'.format(self.name,self.year,self.class_num,self.student_id)

student_1 = Student('김인호',2,3,35)

print(Student.introduce_myself(Student('김인호',2,3,35)))

#문제4. 위 gun class의 메소드들을 static me
class Gun1():
    bullet = 0
    @staticmethod
    def shoot(num):
        for i in range(num) :
            if Gun1.bullet>=1 :
                print('탕!')
                Gun1.bullet -= 1
            elif Gun1.bullet == 0 :
                print('총알이 없습니다!')
                break
    @staticmethod
    def charge(num):
        Gun1.bullet = num
        print('{} 발이 장전되었습니다.'.format(num))
    @staticmethod
    def print():
        print('{} 발 남았습니다.'.format(Gun1.bullet))

class Gun2():
    def __init__(self):
        self.bullet = 0
    def shoot(self, num):
        for i in range(num) :
            if self.bullet>=1 :
                print('탕!')
                self.bullet -= 1
            elif self.bullet == 0 :
                print('총알이 없습니다!')
                break
    def charge(self, num):
        self.bullet = num
        print('{} 발이 장전되었습니다.'.format(num))
    def print(self):
        print('{} 발 남았습니다.'.format(self.bullet))

print('Gun1 class\n')
print('gun0')
gun0 = Gun1()
gun0.charge(10)
gun0.shoot(3)
gun0.print()

print('\ngun1')
gun1 = Gun1()
gun1.shoot(3)
gun1.print()

print('\nGun2 class\n')
print('gun2')
gun2 = Gun2()
gun2.charge(10)
gun2.shoot(3)
gun2.print()

print('\ngun3')
gun3 = Gun2()
gun3.charge(10)
gun3.shoot(3)
gun3.print()

#문제5. static method로 선언한 두개의 클래스를 이용해서 인스턴스화 한 두개의 총의 쏘는 메소드가 서로 같은 메모리를 쓰는지 다른메모리를 쓰는지.
print(gun0.shoot)
print(gun1.shoot)

print(gun2.shoot)
print(gun3.shoot)


#예제:
class sample(object):
    def __call__(self):
        print("생성하면 바로 실행되요")

sample = sample()
sample()
#클래스를 데코레이터로 구현아는 예제

from functools import wraps

class onlyadmin(object):     #함수에 들어가는 매개변수의 문자열을 받아서
    def __init__(self,func): #대문자로 변환해주며 함수를 실행하는 클래스
        self.func = func

    def __call__(self,*args,**kwargs):
        name = kwargs.get('name').upper()
        self.func(name)

@onlyadmin
def greet(name):
    print("Hello {}".format(name))

greet(name='Scott')

#문제4. 위의 onlyadmin 데코레이터 활용해서 find_job함수를 강력하게 하시오.

class onlyadmin(object):     #함수에 들어가는 매개변수의 문자열을 받아서
    def __init__(self,func): #대문자로 변환해주며 함수를 실행하는 클래스
        self.func = func

    def __call__(self,*args,**kwargs):
        name = kwargs.get('name').upper()
        self.func(name)

import pandas as pd
@onlyadmin
def find_job(name):
    emp = pd.DataFrame.from_csv("d:/data/emp.csv")
    print('당신의 직업은 {}입니다.'.format(emp[['job']][emp['ename']==name].values[0][0]))

find_job(name='scott')


x=[1,2,3]
next(x)
print(type(x))
y=iter(x)
print(type(y))
next(y)

from abc import ABCMeta,abstractmethod
class Animal(object):
    __metaclass__ = ABCMeta

    @abstractmethod #추상메소드 선언
    def bark(self):  # 비어있는 메소드이지만 굉장히 중요한 메소드, 상속 받는 자식들이 반드시 구현해야 하는.
        pass

class Cat(Animal):
    def __init__(self):
        self.sound='야옹~'

    def bark(self):
        return self.sound


class Dog(Animal):
    def __init__(self):
        self.sound='멍멍!'
    def bark(self):
        return self.sound

cat =Cat()
dog =Dog()
cat.bark()
dog.bark()

#문제5. 음료라는 추상클래스를 생성하고 아메리카노와 카페라떼 클래스를 자식 클래스로 생성하시오.
from abc import ABCMeta,abstractmethod
class Beverage(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def cost(self):
        pass

class CafeLatte(Beverage):

    def __init__(self):
        self.cos = 4.0

    def cost(self):
        return self.cos

class Americano(Beverage):
    def __init__(self):
        self.cos=3.5

    def cost(self):
        return 'americano',self.cos

americano = Americano()
cafelatte = CafeLatte()
print(americano.cost())



