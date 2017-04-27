# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:51:24 2017

@author: stu
pandas 연습
"""

#문제1. 직업이 salesman인 사원들의 이름과 월급 직업
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result= emp[['ename','sal','job']][emp['job']=='SALESMAN']
print(result)

import csv
file = open(r"D:\data\emp2.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[2]=='SALESMAN':
        print(i[1],i[5])
        
#문제2. 직업이 salesman, analyst 인 사원들의 이름과 월급, 직업
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp[ ['ename','sal','job'] ][emp['job'].isin(['SALESMAN','ANALYST']) ] #isin(리스트변수)
print(result)

#문제3. 직업이 salesman, analyst가 아닌 사원들의 이름과 월급과 직업
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp[ ['ename','sal','job'] ][~emp['job'].isin(['SALESMAN','ANALYST'])]
print(result)

import csv
file = open(r"D:\data\emp2.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[2] not in ['SALESMAN','ANALYST']:
        print(i[1],i[5])

#문제4. 커미션이 null인 사원 이름 커미션

import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp_comm.csv")
result = emp[ ['ename','comm'] ][emp['comm'].isnull()]
print(result)

#문제5. 커미션이 널이 아닌 사원 이름 커미션
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp_comm.csv")
result = emp[ ['ename','comm'] ][emp['comm'].notnull()]
print(result)

import csv
file = open(r"D:\data\emp2_comm.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[6] != '':
        print(i[1],i[5])


#문제6. 월급이 1000에서 3000사이인 사원들의 이름과 월급을 출력하시오.
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp_comm.csv")
result = emp[ ['ename','sal'] ][(emp['sal']>=1000) & (emp['sal']<=3000)]
print(result)

import csv
file = open(r"D:\data\emp2_comm.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    if int(i[5]) >= 1000 and int(i[5])<=3000:
        print(i[1],i[5])

#문제7. 이름의 첫 글자가 S로 시작하는 사원들의 이름을 출력
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp_comm.csv")
result = emp[ ['ename','sal'] ][emp['ename'].apply(lambda x:x[0]=='S')]
print(result)

import csv
file = open(r"D:\data\emp2_comm.csv")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[1][0:1]=='S':
        print(i[1])

def hap(x,y):
    return x+y

hap(10,20)
# 이 코드를 lambda 표현식으로 하면?
print((lambda x,y:x+y)(10,20))

#문제8. 위 문제를 lambda 쓰지 않고 함수를 생성해서
def ss(target):
        return target[0:1]

import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp_comm.csv")
result = emp[ ['ename','sal'] ][emp['ename'].apply(ss(emp['ename'])=='S')]
print(result)


print(ss('ename'))

#람다로 하는게 좋다..

#문제9. 이름의 끝글자가 T로 끝나는 사원들 이름
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp_comm.csv")
result = emp[ ['ename','sal'] ][emp['ename'].apply(lambda x:x[-1]=='S')]
print(result)

#문제10. 직업, 직업별 최대월급을 출력하되 직업이 salesman 제외
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv") 
emp = emp[['job','sal']][emp['job']!='SALESMAN']
result = emp.groupby('job')['sal'].max()
print(result)

#문제11. 부서번호, 직업, 부서번호별 직업별 토털월급
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv") 
result = emp.groupby(['deptno','job'])['sal'].sum()
print(result)

#(pandas이용 서브쿼리) 문제12. jones보다 더 많은 월급을 받는 사원들의 이름과 월급을
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
subq = emp[['sal']][emp['ename']=='JONES'].values[0]
print(type(subq))
emp = emp[['ename','sal']][emp['sal']> subq[0]]
print (emp)

#문제13. scott의 직속상사 이름
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
subq = emp[['mgr']][emp['ename']=='SCOTT'].values[0]
result = emp[['ename']][emp['empno']==subq[0]]
print(result)

#문제14. 관리자인 사원들의 이름
import pandas as pd
emp = pd.read_csv(r"D:\data\emp_comm.csv")
subq = emp[['mgr']]
result = emp[['ename']][emp['empno'].isin(emp['mgr'])]
print(result)

#문제15. 컬럼 c5,c6,c8이 남아있을 때 어떤 수가 가장 좋은 수 인가.

import pandas as pd
ttt = pd.DataFrame.from_csv(r"D:\data\ttt.csv")

result1 = ttt[(ttt['PLAYER']==1) &
              (ttt['C1']==1) &
              (ttt['C2']==2) &
              (ttt['C3']==1) &
              (ttt['C4']==2) &
              (ttt['C7']==1) &
              (ttt['C9']==2) &
              (ttt['C5']+ttt['C6']+ttt['C8']==1)]
              
result2 = result1.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max()

import pandas as pd
ttt = pd.DataFrame.from_csv(r"D:\data\ttt.csv")
result3 = ttt[(ttt['PLAYER'])==1 & ttt['LEARNING_ORDER'].isin(result2.tolist())]
print(result3)

#문제16. 딕셔너리 이용하여 주어가 0, 명사가 2, 동사 1 로해서 한글과 영문을 저장하시오.
dic={}
dic['나는']=('I',0)
dic['소년']=('boy',2)
dic['이다']=('am',1)
dic['피자']=('pizza',2)
dic['먹는다']=('eat',1)

dic['나는'][1]

#문제17. 한글을 물어보게 하고 한글을 입력하면 영어로 번역하는 프로그램을 작성
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)) :
    for j in input_list :
        if dic[j][1]==i :
            result = result + dic[j][0] + ' '
print(result)


#문제18. 감성어 사전을 불러오시오.
import csv
file = open(r"D:\data\smt_dic.csv")
smt = csv.reader(file)

for i in smt:
    print(i)

#문제19. 위에서 1,3,4요소 출력
import csv
file = open(r"D:\data\smt_dic.csv")
smt = csv.reader(file)

for i in smt:
    print(i[1],i[3],i[4])

#문제20. 사전의 1번째 요소를 key, 3번째 요소를 value의 0번째, 4번째를 value의 1번째
import csv
file = open(r"D:\data\smt_dic.csv")
smt = csv.reader(file)
smt_dic = {}
for i in smt:
    smt_dic[i[1]]=(i[3],i[4])
    smt_dic[i[2]]=(i[3],i[4])

#문제21. 위 사전을 이용하여 한글영문 번역기를 완성시키시오.
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)) :
    for j in input_list :
        if smt_dic[j][1]==i :
            result = result + smt_dic[j][0] + ' '
print(result)

#문제22. 다음에 둘 가장 좋은수를 찾는 프로그램

c1=input('C1 : (1 OR 2)')
c2=input('C2 : ')
c3=input('C3 : ')
c4=input('C4 : ')
c5=input('C5 : ')
c6=input('C6 : ')
c7=input('C7 : ')
c8=input('C8 : ')
c9=input('C9 : ')


import pandas as pd
ttt = pd.DataFrame.from_csv(r"D:\data\ttt.csv")

result1 = ttt[(ttt['PLAYER']==1) &
              (ttt['C1']==0) &
              (ttt['C2']==0) &
              (ttt['C3']==0) &
              (ttt['C4']==0) &
              (ttt['C5']==0) &
              (ttt['C6']==0) &
              (ttt['C7']==0) &
              (ttt['C8']==0) &
              (ttt['C9']==0) &
              (ttt['C1']+ttt['C2']+ttt['C3']+ttt['C4']+ttt['C5']
              +ttt['C6']+ttt['C7']+ttt['C8']+ttt['C9']==1)]
              
result2 = result1.groupby(['C1','C2','C3','C4','C5','C6','C7','C8','C9'])['LEARNING_ORDER'].max()

import pandas as pd
ttt = pd.DataFrame.from_csv(r"D:\data\ttt.csv")
result3 = ttt[(ttt['PLAYER'])==1 & ttt['LEARNING_ORDER'].isin(result2.tolist())]
print(result3)



7//2