# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:51:05 2017

@author: stu
"""

#예제1) 홀수는 출력되지 않게 하시오
for i in range(1,10):
    if i%2==1:
        continue
    print(i)
#문제1. 숫자를 1부터 10까지 출력하는데 중간에 5는 나오지 않게 하시오.
for i in range(1,11):
    if i==5:
        continue
    print(i)

#예제2) 무한루프문을 break를 사용하여 정지하시오.
i=0
while(True):
    i+=1
    if i==1000:
        print('i가 {0}이 됨. 반복문을 중단함.'.format(i))
        break
    print(i)

#문제2. 함수를 생성하는데 아래와 같이 숫자를 넣어서 실행하면 해당 숫자만큼 숫자가 세로로 출력되게.
def break_fun(num1):
    i=0
    while(True):
        i+=1
        print(i)
        if i==num1:
            break
        
print(break_fun(10))

#문제3. 위 함수 수정하여 결과가 아래와 같이 가로로 출력
def break_fun(num1):
    i=0
    while(True):
        i+=1
        print(i,end=' ')
        if i==num1:
            break
        
print(break_fun(10))
#문제4. 아래와 같이 딕셔너리 형태의 데이터를 만들고 출력하시오.
emp_dic = {'mgr':7788,'sal':'1100','deptno':20,'comm':'0','job':'CLERK',
           'hiredate':'1983-01-15','empno':7876,'ename':'ADAMS'}

print(type(emp_dic))

for i in emp_dic:
    print(i)

#문제5. for loop를 이용하여 emp2.csv를 읽어와서 dict 형태로 
import csv
emp_csv = csv.reader(open(r"D:\data\emp_comm.csv"))
emp_dic =[]
for i in emp_csv:
    emp_dic.append(i)
    if i[7]=='deptno':
        break
              

emp_dic = {'mgr':i[0],
               'ename':i[1]}
default_data = {
            'item1': 1,
            'item2': 2,
}
default_data['item3'] = 3
default_data.update({'item3': 3})

#문제6. emp 딕셔너리 변수에서 이름만 출력하시오.

import csv
emp_csv = csv.reader(open(r"D:\data\emp2.csv"))
emp_dic =[]

for i in emp_csv:
    emp_dic.append({'empno':i[0],'ename':i[1],'job':i[2],'mgr':i[3],
                    'hiredate':i[4],'sal':i[5],'comm':i[6],'deptno':i[7]})

for i in emp_dic:
    print(i['ename'])

#문제7. 이름, 월급, 직업
for i in emp_dic:
    print(i['ename'],i['sal'],i['job'])


#문제8. dept.csv 읽어서 딕셔너리로 저장.

import csv
dept_csv = csv.reader(open(r"D:\data\dept2.csv"))
dept_dic=[]

for i in dept_csv:
    dept_dic.append({'deptno':i[0],'dname':i[1],'loc':i[2]})


for i in dept_dic:
    print(i['deptno'],i['dname'],i['loc'])


#문제9. emp.csv와 dept.csv를 각각 읽어와서 emp_dic, dept_dic 딕셔너리 자료형으로 만드는 스크립트를 하나로 합치시오.
import csv
emp_csv = csv.reader(open(r"D:\data\emp2.csv"))
emp_dic =[]

import csv
dept_csv = csv.reader(open(r"D:\data\dept2.csv"))
dept_dic=[]

for i in dept_csv:
    dept_dic.append({'deptno':i[0],'dname':i[1],'loc':i[2]})

for i in emp_csv:
    emp_dic.append({'empno':i[0],'ename':i[1],'job':i[2],'mgr':i[3],
                    'hiredate':i[4],'sal':i[5],'comm':i[6],'deptno':i[7]})


print(emp_dic)
print(dept_dic)


#문제10. empp와 dept라는 딕셔너리 자료구조를 만드는 스크립트와 중첩 for loop문을 이용해서 emp,dept 조인하여 ename,loc출력
for e in emp_dic:
    for d in dept_dic:
        if e['deptno']==d['deptno']:
            print(e['ename'],d['loc'])#오라클의 nested loop 조인 방법의 로직
            
#문제11. 부서위치가 DALLAS인 사원의 이름과 부서위치를 출력하시오.
for e in emp_dic:
    for d in dept_dic:
        if e['deptno']==d['deptno'] and d['loc']=='DALLAS':
            print(e['ename'],d['loc'])

#문제12. 위의 스크립트를 이용해서 조인 함수를 생성하시오
def join(table1,col1,table2,col2,connect_column):
    
    for e in table1:
        for d in table2:
            if e[connect_column]==d[connect_column]:
                print(e[col1],d[col2])


join(emp_dic,'ename',dept_dic,'loc','deptno')


#문제13. pandas를 이용하여 이름, 부서위치 출력
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
dept = pd.read_csv(r"D:\data\dept.csv")

result=pd.merge(emp,dept,on='DEPTNO')
print (result[['ename','LOC']])

#문제14. 부서위치가 DALLAS인 사원들의 이름과 부서위치를 출력하시오.
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
dept = pd.read_csv(r"D:\data\dept.csv")

result=pd.merge(emp,dept,on='DEPTNO')
print (result[['ename','LOC']][result['LOC']=='DALLAS'])

#문제15. 이름, 부서위치를 출력하는데 outer join
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
dept = pd.read_csv(r"D:\data\dept.csv")

result = pd.merge(emp,dept,on='DEPTNO',how='outer')
print(result[['ename','LOC']])

#예제1. 
def my_abs(arg):
    if(arg<0):
        result = arg*-1
    else:
        result = arg
    return result

my_abs(-1)

#문제16. 아래와 같이 이름을 입력해서 함수를 실행하면 해당 사원의 부서위치가 출력되게.
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
dept = pd.read_csv(r"D:\data\dept.csv")

def findloc(ename):
    import pandas as pd
    result = pd.merge(emp,dept,on='DEPTNO')
    result = result[['ename','LOC']][result['ename']==ename.upper()]
    return result

findloc('scott')

#문제17. 미분계수를 구하는 함수를 생성하는데  #함수 f(x)=2x^2+1일때 x=-2일때 기울기를 구하시오.
def diff(num):
    result = (2*pow((num+0.0001),2)+1-(2*pow(num,2)+1))/0.0001
    return result

diff(-2)

#예제) 미분함수
def numerical_diff(f,x):
    delta = 1e-4 
    return ( f(x+delta)-f(x-delta))/(2*delta)

#함수(2x^2+1) 생성
def function_1(x):
    return 2*pow(x,2)+1

print(numerical_diff(function_1,-2))

def mibun_fun(a):
    f = lambda x : 2*(x**2) +1 
    return round((f(a+0.001)-f(a))/0.001)
print(mibun_fun(-2))

#문제18. f(x)=x^2-x+5 함수의 x=-2일때 미분계수
def numerical_diff(f,x):
    delta = 1e-4 
    return ( f(x+delta)-f(x-delta))/(2*delta)
def function_1(x):
    return 2*x**2+1

print(numerical_diff(function_1,-2))




