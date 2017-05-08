#중급알고리즘 문제1
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




