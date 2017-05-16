

def decode(length,code):
    alphabet=[
     ['0','0','0','0','0','0','A']
    ,['0','0','1','1','1','1','B']
    ,['0','1','0','0','1','1','C']
    ,['0','1','1','1','0','0','D']
    ,['1','0','0','1','1','0','E']
    ,['1','0','1','0','0','1','F']
    ,['1','1','0','1','0','1','G']
    ,['1','1','1','0','1','0','H']]
    target='{0}'.format(code)
    arr=[]
    word=''
    matchcnt=0
    for i in range(len(target)):
        arr.append(target[i:i+1])

    for k in range(1,length+1):
        arr2=arr[6*(k-1):6*k]
        word2=word
        for i in range(8):
            for j in range(6):
                if alphabet[i][j]==arr2[j]:
                    matchcnt+=1
            if matchcnt>=5:
                matchcnt = 0
                word+=alphabet[i][6]
                break
            else:
                matchcnt=0
        if word2==word:
            return k
            break

    return word

decode(5,'011111000000111111000000111111')
decode(3,'001111000000011100')


#중급 알고리즘 문제2 숫자 야구

def baseball(num):
    target = ['3','2','4']


k=['a','a','b']
for i in k:
    print(i)


a=['1','2','3','4','5']

b=dict(a)

b.update(i)
for i in a:
    b={i}
c=0
for i in a:
    b[c]=i
    c+=1

print(b)

target=['3','2','4']
numb = ['1','2','3','4','5','6','7','8','9']

b = int(input("#1 : "))
for i in range(b):
    d = []
    c = input("# : ")
    e = c.split(' ')
    for j in range(len(e[0])):
        d.append(e[0][j:j+1])
        for k in range(3):



print(b)

c='123 1 1'
e=c.split(' ')
d=[]
for i in range(len(e[0])):
    d.append(e[0][i:i+1])
print(d)

c='123'
d=[]
for i in range(len(c)):
    d.append(c[i:i+1])


def algor(seq,sum):
    def pibo(n, num):
        gap = 1000
        pib_seq = [1, 1]
        for i in range(n - 3):
            pib_seq.append(pib_seq[i] + pib_seq[i + 1])
        a = pib_seq[len(pib_seq) - 2]
        b = pib_seq[len(pib_seq) - 1]
        x_max = (num - b) // a + 1
        y_max = (num - a) // b + 1
        for x in range(x_max):
            for y in range(y_max):
                if a * x + b * y == num:
                    if x < y:
                        if gap > y - x:
                            gap = y - x
                            x_a = x
                            y_a = y
        return x_a, y_a




import timeit
start = timeit.default_timer()

for x in range(1,43):
    for y in range(1,27):
        if 5*x+8*y==218:
            if x<y:
                print(x,y)

function_to_test(300000)


stop = timeit.default_timer()
print(stop - start)

for x in range(1,13):
    for y in range(1,8):
        if 3*x+5*y==41:
            print(x,y)
            break


a = 1
b=[1,1]
for i in range(4):
    b.append(b[i]+b[i+1])
b

from memory_profiler import profile
@profile
def pibo(n,num):
    gap=1000
    pib_seq=[1,1]
    for i in range(n-3):
        pib_seq.append(pib_seq[i]+pib_seq[i+1])
    a=pib_seq[len(pib_seq)-2]
    b=pib_seq[len(pib_seq)-1]
    x_max=(num-b)//a+1
    y_max=(num-a)//b+1
    for x in range(x_max):
        for y in range(y_max):
            if a*x+b*y==num:
                if x<y:
                    if gap>y-x:
                        gap=y-x
                        x_a=x
                        y_a=y
    return x_a,y_a

pibo(7,218)
pibo(6,41)

import math
3//2

pib_seq=[1,1]
for i in range(3):
    pib_seq.append(pib_seq[i]+pib_seq[i+1])
a=pib_seq[len(pib_seq)-2]
b=pib_seq[len(pib_seq)-1]
x_max=(41-b)//a
y_max=(41-a)//b

print(x_max)
print(a)

for x in range(1,13):
    for y in range(1,8):
        if 3*x+5*y==41:
            if x<y:
                print(x,y)

#####
size = int(input('Size : '))
arr = []
for i in range(size):
    arr.append(list(input('Row{0} : '.format(i)).replace(' ','')))
for i in range(len(arr)):
    print(arr[i])
total = 0
for row in range(size):
    for col in range(len(arr[0])):
        total += int(arr[row][col])
    if total % 2 ==0:
        total = 0










