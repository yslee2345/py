import pandas as pd
file = pd.read_csv(r'D:\data\fitness.csv')
file[['Weight']].mean()



#############함 수 정 의##############
def substr(su1,su2,su3):
    return(su1[su2:su3])



def Equal(input_list,list):  001111 000000
        cnt = 0
        for i in range(0,6):
            if input_list[i] != list[i]:
                cnt+=1
        if (cnt > 1):
            return False
        return True

#####################################
#############변 수 선 언##############
list=[(65,'000000'),(66,'001111'),(67,'010011'),(68,'011100'),
      (69,'100110'),(70,'101001'),(71,'110101'),(72,'111010')]
input_list=[] # input2 의 암호를 6자리씩 담을 리스트
list_row = ''  # list(i,j) 에서 i 즉, 행 값을 담을 변수
check=False
#####################################

input1=int(input('문자의 개수 입력 : '))
input2=input('전달할 암호 입력 : ')

for i in range(0,input1):
    tmp = substr(input2,i * 6, (i + 1) * 6) # tmp 변수에 6자리씩 자른 값을 담는다
    input_list.append(tmp) # 그 자른 값을 input_list에 담는다
[001111,000000,000000]

for i in range(0,input1): # 0 ~ 문자의 개수
    for j in range(0,8):
        if Equal(input_list[i],list[j][1]): # i = 0 ~ 문자의 개수 , j = 0 ~ 8
            list_row += chr(list[j][0]) # 암호 해독한 문자를 합친다
            break


