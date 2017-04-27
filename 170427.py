#Public member
class yourClass:
    pass


class myClass:
    def __init__(self):
        self.message = "Hello"
        self.__private="private"


    def some_method(self):

        print(self.message)
        print(self.__private)

obj = myClass()
obj.some_method()
print(obj.__private)

#inheritance
class father:
    def base_method(self):
        print("hello")

class child(father):
    pass

father = father()
father.base_method()
child = child()
child.base_method()

#상속 예제
#init 메소드 가지고 실행하는데 부모와는 다르게 자식에 message라는 속성이 없어서 상속시키고 싶을때?
class father1:
    def func(self):
        print("지식")

class father2:
    def func(self):
        print("지혜")

class child(father1,father2):
    def childfunc(self):
        father1.func(self)
        father2.func(self)

child = child()
child.func()
#다이아몬드 상속
class GrandFather:
    def __init__(self):
        print("튼튼한 두 팔")

class Father1(GrandFather):
    def __init__(self):
        super().__init__()
        print("지식")

class Father2(GrandFather):
    def __init__(self):
        super().__init__()
        print("지혜")

class GrandChild(Father1,Father2):
    def __init__(self):
        super().__init__()
        print("자기 만족도가 높은 삶")



grandchild = GrandChild()
grandchild.__init__()

#문제1.

class GrandFather:
    def __init__(self):
        print("두팔")
class Father2(GrandFather):
    def __init__(self):

        print("지혜")

father2=Father2()
#여기에서 지혜만 나온다는 것은 오버라이드 되었다는 의미.
#super
class GrandFather:
    def __init__(self):
        print("두팔")


class Father2(GrandFather):
    def __init__(self):
        super().__init__()
        print("지혜")

father2=Father2()

def greet(name):
    return "Hello {0}".format(name)

greet_someone =greet
print(greet_someone("SCOTT"))


def greeting(name):
    def greet_msg():
        return "Hello"
    return "{} {}".format(greet_msg(),name)

print(greeting("SCOTT"))

def greet(name):
    return "Hello {}".format(name)

def change_name_greet(func):
    name = "King"
    return func(name)

print(change_name_greet(greet))

def greet(name):
    return "Hello {}".format(name)

def uppercase(re):
    def wrapper(name):
        result = re(name)
        return result.upper()
    return wrapper

new_greet = uppercase(greet)
print(new_greet("SCOTT"))

#문제2 이름을 입력하고 함수를 실행하면 해당하는 사원의 직업이 소문자로 출력되는 함수.
def find_job(name):
    if name == 'SCOTT':
        return "{}".format(name)

def lowercase(val):
    def wrapper(name):
        result = 'ANALYST'
        return result.lower()
    return wrapper

new_find_job = lowercase(find_job)
print(new_find_job('SCOTT'))


def find_job(name):
    return "{}".format(name)

def lowercase(val):
    def wrapper(name):
        import csv
        file = open(r"D:\data\emp2.csv")
        emp_csv = csv.reader(file)
        for i in emp_csv:
            if i[1] == name:
                result = i[2]
                return result.lower()
    return wrapper

new_find_job = lowercase(find_job)
print(new_find_job('SCOTT'))

def find_job(name):
    import csv
    file = open(r"D:\data\emp2.csv")
    emp_csv = csv.reader(file)
    for i in emp_csv:
        if i[1]==name:
            return i[2]

def lowercase(val):
    def wrapper(name):
        return find_job(name).lower()
    return wrapper

new_find_job = lowercase(find_job)
print(new_find_job('JONES'))

class Greet(object):
    current_user=None
    def set_name(self,name):
        if name=='admin':
            self.current_user=name
        else:
            raise Exception("No grant")

    def get_greeting(self,name):
        if name=='admin':
            return "Hello {}".format(self.current_user)

greet = Greet()
greet.set_name('admin')
print(greet.get_greeting('admin'))

#위 코드에서 중복적으로 사용되는 코드를 뗴어내서 함수로 생성.

def is_admin(user_name):
    if user_name != 'admin':
        raise Exception('No grant')

class Greet(object):
    def is_admin(user_name):
        if user_name != 'admin':
            print("no grant")

    current_user=None


    def set_name(self,name):
        is_admin(name)
        self.current_user=name

    def get_greeting(self,name):
        is_admin(name)
        return "Hello {}".format(self.current_user)

greet = Greet()
print(greet.get_greeting('admin'))

#문제. 이름을 넣어서 함수를 실행하면 해당 사원의 월급이 출력되게 하는 함수를 생성하는데 KING만 월급을 볼 수 있게하고 KING이 아닌 다른 사원들은 권한이 없다면서 볼 수 없게.

import pandas as pd
def is_king(user_name):
    if user_name !='KING':
        raise Exception('No grant')

class ShowSal(object):
    current_user = None

    def set_name(self,name):
        is_king(name)
        self.current_user=name

    def get_sal(self,name):
        is_king(name)
        emp = pd.DataFrame.from_csv("d:/data/emp.csv")
        sal = emp[['sal']][emp['ename'] == name].values[0][0]
        return sal

showsal = ShowSal()
print(showsal.get_sal('KING'))



import pandas as pd
def is_admin(user_name):
     if user_name != 'KING':
          raise Exception("권한이 없다니까요 ")

class find_sal(object):
     current_user = None
     def set_name(self,name):
         is_admin(name)
         self.current_user = name

     def get_sal(self,name):
         is_admin(name)
         emp = pd.DataFrame.from_csv("d:/data/emp.csv")
         sal= emp[['sal']][emp['ename'] == name].values[0][0]
         return sal

find_sal  = find_sal ()
find_sal.set_name('KING')
print(find_sal.get_sal('KING') )

#문제. 다음 코드를 데코레이터로
def is_admin(func):
    def wrapper(*arg,**kwargs): #*arg 가변 매개변수, **kwargs 딕셔너리 가변 매개변수
        if kwargs.get('name') != 'admin':
            raise  Exception('No grant')
        return func(*arg,**kwargs)
    return wrapper

class Greet(object):
    current_user=None

    @is_admin
    def set_name(self,name):
        self.current_user=name

    @is_admin
    def get_greeting(self,name):
        return "Hello {}".format(self.current_user)

greet = Greet()
greet.set_name(name='admin')
print(greet.get_greeting(name='admin'))


#문제. 데코레이터 함수로 코드를 좋게 개선
def is_admin(func):
    def wrapper(*arg,**kwargs): #*arg 가변 매개변수, **kwargs 딕셔너리 가변 매개변수
        if kwargs.get('name') != 'admin':
            raise  Exception('No grant')
        return func(*arg,**kwargs)
    return wrapper
######################

import pandas as pd
def is_admin(func):
    def wrapper(*arg,**kwargs):
        if kwargs.get('name')!='KING':
            raise Exception('No grant')
        return func(*arg,**kwargs)
    return wrapper

class find_sal(object):
     current_user = None
     @is_admin
     def set_name(self,name):
         self.current_user = name
     @is_admin
     def get_sal(self,name):
         emp = pd.DataFrame.from_csv("d:/data/emp.csv")
         sal= emp[['sal']][emp['ename'] == name].values[0][0]
         return sal

find_sal  = find_sal ()
find_sal.set_name(name='SCOTT')
print(find_sal.get_sal(name='SCOTT'))

import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
sal= emp[['sal']][emp['ename'] == 'KING'].values[0][0]
print(sal)



