# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:55:05 2017

@author: stu
"""

#문제1. 직업이 salesman, 월급이 1200 이상인 사원들의 이름과 직업 월급

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if (i[2]=='SALESMAN') & (int(i[5])>=1200):
        print(i[2],int(i[5]))
        
#문제2. 월급이 1000에서 3000사이인 사원들의 이름과 월급을 출력하시오!

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if (int(i[5])>1000) & (int(i[5])<3000):
        print(i[1],int(i[5]))


#문제3. 직업이 ANALYST, CLERK인 사원들의 이름과 월급과 직업을 출력하시오

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if (i[2]=='ANALYST') | (i[2]=='CLERK'): #혹은 i[2] in ['ANALYST','CLERK']
        print(i[1],i[2])

#문제4. 직업이 ANALYST, CLERK이 아닌 사원들의 이름과 월급

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if i[2] not in ['ANALYST','CLERK']:
        print(i[1],i[2])
#문제5. 커미션이 null인 사원들의 이름과 커미션을 출력하시오
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if i[6] == '': 
        print(i[1],i[2])
#문제6. 커미션이 null이 아닌 사원들의 이름과 커미션
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if i[6] != '': 
        print(i[1],i[2])
        
#문제7. 이름의 첫번째 철자가 S 로 시작하는 사원들의 이름과 월급
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if i[1][0:1] == 'S': 
        print(i[1],i[2])
        
#문제8. 이름의 두번쨰 철자가 M인 사원들의 이름과 월급을 출력하시오
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    if i[1][1:2] == 'M': 
        print(i[1],i[2])
  
#문제9. 이름의 마지막 철자가 H인 사원들의 이름과 월급을 출력
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for i in emp_csv:
    j=len(i[1])
    if i[1][j-1:j]=='H':      #혹은 i[1][-1]=='H': 이런식으로 끝에서 두번째 철자는 -2
        print(i[1],i[2])
    
#문제10. a 라는 비어있는 리스트 변수를 선언하고 input 명령어를 이용해서 a 리스트 변수에 요소를 추가하시오


a=[]
b=input("요소를 입력")    
a.append(b)    
    
#문제11. 리스트 변수에 추가된 요소를 삭제하는 코드를 구현하시오.    
    
b=input("삭제할 요소를 입력")    
a.remove(b)   
    
#문제12. 리스트 변수에 요소를 추가하고 삭제하고 갯수를 확인하는 코드를 구현


c=input("추가하려면 1, 삭제하려면 2, 갯수확인은 3")
c=int(c)

if c==1:
    b=input("추가할 요소 입력하세요")
    a.append(b)
elif c==2:
    b=input("삭제할 요소 입력하세요")
    a.remove(b)
else:
    b=a.count(a)
    print(b)
    
#문제13. 리스트 메소드 중에 sort를 이용해서 월급을 출력할 떄 높은것 부터 출력될 수 있도록 하시오!
#(sal_list 라는 비어있는 리스트에 emp_list에 5번째 요소를 for loop로 담아낸다)
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
sal_list =[]
for i in emp_csv:
    sal_list.append(i[5])
    
    
    
    
print(sal_list.sort())    
    
#문제14. 위 코드를 활용해서 이름과 월급 출력하는데 월급 높은것부터    
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
sal_list =[]
for i in emp_csv:
    sal_list.append(int(i[5]))
    
sal_list.sort(reverse=True) 
    
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for j in sal_list:
    for i in emp_csv:
        if int(i[5])==j:
            print(i[1],i[5])
     
            
    
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)


for i in emp_csv: 
    print(i[5])
    
for j in sal_list:
    print(j)
    
def salcheck(data):
    return int(data[5]) 
print (salcheck(sal_list))   

#문제15. 이름과 월급을 출력하는데 이름을 abcd순서대로 출력되게 하시오.

import csv

def salCheck(data):
    return data[1]

file = open("D:\data\emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=False, key=salCheck)

for i in emp_list_sorted:
    print(i)

#문제16. 직업이 SALESMAN인 사원들의 이름과 입사일과 직업을 출력하는데 최근에 입사한 사원부
import csv

def salCheck(data):
    return data[4]

file = open("D:\data\emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=True, key=salCheck) #reverse = true면 내림차

for i in emp_list_sorted:
    if i[2]=='SALESMAN':
        print(i)

#문제17. emp_list에서 최대월급을 출력하시오

import csv

file = open("D:\data\emp2.csv", "r")
emp_csv = csv.reader(file)
sal_list=[]
for i in emp_csv:
    sal_list.append(int(i[5]))

print(max(sal_list))

#문제18. emp_list에서 월급의 평균값

import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
sal_list = []
for i in emp_csv:
    sal_list.append(int(i[5]))
    
print(sum(sal_list)/len(sal_list))

#문제19. emp_list에서 직업이 SALESMAN인 사원들 중에서의 최대월급을 출력
import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    if i[2]=='SALESMAN':
        emp_list.append(i[5])

print(max(emp_list))

#문제20. 아래와 같은 상황일떄 player1이 둘떄 가장 유리한수가 무엇인가.(SQL)
# 1  2  1
# 2  0  0
# 1  0  2

#문제21. mit_ttt_학습데이터_csv파일의 파일명을 간단하게 변경하고 전체 데이터를 파이선에서 출력하시오.

for i in open(r"D:\data\ttt.txt",'r'):
    print(i)
    
#문제22. pandas 모듈을 이용해서 사원 테이블에서 최대 월급을 출력하시오
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
print(emp['sal'].max()) 

#문제23. 직업이 salesman인 사원들의 이름과 월급과 직업을 출력하시오.
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp[['ename','sal']][emp['job']=='SALESMAN']
               #열                  #행
print(result)

#문제24. 월급이 3000이상인 사원들의 이름과 월급
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp[['ename','sal']][emp['sal']>=3000]
print(result)

#문제25. 위 결과에서 월급이 낮은 순으로
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp[['ename','sal']][emp['sal']>=3000].sort_values('sal',ascending=True)
print(result)

#문제26. 부서번호가 20번인 사원들의 최대월급을 출력하시오
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp['sal'][emp['deptno']==20].max() #pandas를 이용할땐 index역할을 할 컬럼이 있어야 한다. 그래서 empno가 같이 출력됨.
print(result)

#문제27. 직업, 직업별 토털월급
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp.groupby('job')['sal'].sum() #pandas를 이용할땐 index역할을 할 컬럼이 있어야 한다. 그래서 empno가 같이 출력됨.
print(result)

#loop문으로 뽑아보기.

#문제28. 부서번호, 부서번호별 평균월급
import pandas as pd
emp = pd.DataFrame.from_csv(r"D:\data\emp.csv")
result = emp.groupby(['deptno','job'])['sal'].mean()
print(result)


#문제29. 밑 쿼리를 pandas 이용하여.
#select max(learning_order) from ttt_data
#                            where player = 1
#                            and c1 = 1 and c2 = 2 and c3 = 1 and c4 = 2 and c7 = 1 and c9 = 2
#                            and c5+c6+c8 = 1
#                            group by c5, c6, c8


import pandas as pd
ttt = pd.DataFrame.from_csv(r"D:\data\ttt.csv")

result = ttt[['LEARNING_ORDER','C5','C6','C8']][(ttt['PLAYER']==1) & (ttt['C1']==1) & (ttt['C2']==2) & 
            (ttt['C3']==1) & (ttt['C4']==2) & (ttt['C7']==1) & (ttt['C9']==2) &
            (ttt['C5']+ttt['C6']+ttt['C8']==1)]


result2 = result.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max()

print(result2)

result3 = result2[['LEARNING_ORDER']]

print(result2[['C5']])
import pandas as pd
ttt = pd.DataFrame.from_csv(r"D:\data\ttt.csv")
print(ttt)


#선생님 코드

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


