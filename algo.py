# A 000000
# B 001111
# C 010011
# D 011100
# E 100110
# F 101001
# G 110101
# H 111010

alphabet=[
    ['0','0','0','0','0','0','A']
,['0','0','1','1','1','1','B']
,['0','1','0','0','1','1','C']
,['0','1','1','1','0','0','D']
,['1','0','0','1','1','0','E']
,['1','0','1','0','0','1','F']
,['1','1','0','1','0','1','G']
,['1','1','1','0','1','0','H']]

target='001111000000011100'

arr=[]
calc=0
for i in range(len(target)):
    arr.append(target[i:i+1])
for k in range(3):
    for i in range(7):
        for j in range(6):
            if alphabet[i][j]==arr[j]:
                calc+=1
        if calc>=5:
            print(alphabet[i][6])
            break
        calc=0



for i in range(len(target)):
    print(i)


