#예제) 예외처리
def my_power():
    try:
        x=input('분자 : ')
        y=input('분모 : ')
        return int(x)/int(y)
    except:
        if ZeroDivisionError:
            return '0으로 나눌수 없습니다.'

my_power()

#문제1. 0으로 나눌수 없습니다 메시지 출력.
def my_power():
    try:
        x=input('분자 : ')
        y=input('분모 : ')
        return int(x)/int(y)
    except:
        if ZeroDivisionError:
            return '0으로 나눌수 없습니다.' # 그냥 print 해도 됨. if 안쓰고.

my_power()

#문제2. 이름을 물어보게하고 이름을 입력하면 해당 사원의 월급이 출력되는 파이썬 코드.
import pandas as pd
def name(names):
    emp = pd.read_csv(r"D:\data\emp_comm.csv")
    result = emp[['sal']][emp['ename']==names.upper()]
    return result

name('kin')

#문제3. 위 코드에 없는 이름을 넣으면 예외처리가 되게.
import pandas as pd
def name():
    emp = pd.read_csv(r"D:\data\emp_comm.csv")
    names = input("사원의 이름?")
    try :
        result = emp[['sal']][emp['ename']==names.upper()].values[0][0]
        return result
    except :
        print('사원이 없습니다.')


name()

#문제4. 이름을 입력하지 않으면 다시 물어보게
import pandas as pd
def name():
    emp = pd.read_csv(r"D:\data\emp_comm.csv")
    names=''
    while names == '':
        names = input("사원의 이름?")
    result = emp[['sal']][emp['ename']==names.upper()].values[0][0]
    return result

name()

#문제5. 없는 사원명을 입력하면 해당 사원은 없습니다. 라고 출력되게.
import pandas as pd
def name():
    emp = pd.read_csv(r"D:\data\emp_comm.csv")
    names=''
    while names == '':
        names = input("사원의 이름?")
    try :
        result = emp[['sal']][emp['ename']==names.upper()].values[0][0]
        return result
    except:
        print('해당 사원은 없습니다.')

name()

#문제6. 직업을 물어보게하고 직업을 입력하면 해당 직업의 토털월급이 출력되게 하는데 아무것도 입력하지 않으면 계속 물어보게하고
#       잘못된 직업을 입력하면 해당 직업 없습니다. 출력
import pandas as pd
def job():
    emp = pd.read_csv(r"D:\data\emp_comm.csv")
    jobs=''
    while jobs=='':
        jobs=input('직업을 입력하세요 :')
    try :
        emp = emp[['job','sal']][emp['job']==jobs.upper()]
        result =emp.groupby('job')['sal'].sum()
        return result
    except :
        print('해당 직업 없음')
    
job()


#예제) 복수개 exception
def my_power():
    try:
        x=input('분자 : ')
        y=input('분모 : ')
        return int(x)/int(y)
    except ZeroDivisionError as err:
        print('00000')
    except:
        print('다른예외')

my_power()
#문제7. (try절을 무사히 실행하면 만날 수 있는 else) 이름을 물어보게하고 해당 사원의 월급이 출력되는데 이름이 없으면
#해당 사원은 없습니다. 라는 메시지 나오게 하고 만약 있어서 성공했다면 월급 추출에 성공했습니다. 라는 메시지 출력
import pandas as pd
def name():
    try :
        names=''
        emp = pd.read_csv(r"D:\data\emp_comm.csv")
        while names == '':
            names = input('이름?')
        result = emp[['sal']][emp['ename']==names.upper()].values[0][0]
        return result
    except Exception as err:
        print('해당 사원 없음.')
    finally:
        print('월급추출 성공')

name()
#문제8. 방금 사용한 else 를 이용하여 아래의 나눈 값을 출력되게 하는데 두수를 물어보게하고 나눈 값을 출력할 때 정상
#적으로 나눠지면 나눈 값을 잘 추출했습니다가 출력되게 하고 0으로 나누면 0으로 나눌 수 없습니다.

def my_power():
    try:
        x=input('분자 : ')
        y=input('분모 : ')
        z=int(x)/int(y)
    except ZeroDivisionError as err:
        print('0으로 나눌 수 없습니다.')
    else:
        print('추출완료')
        return z


my_power()

def my_power():
    try:
        x=input('분자 : ')
        y=input('분모 : ')
        z=int(x)/int(y)
    except Exception as err:#증조할아버지
        print('예외가 발생했습니다.')
    except ZeroDivisionError as err:#증손자자
       print('0으로 못나눔')

class bird:
    def fly(self):
        raise NotImplementedError
class eagle(bird):
    pass
eagle = eagle()
eagle.fly()
#eagle클래스에서 fly함수를 구현하지않아서 에러가 발생.


#문제9. eagle.fly()를 실행할 때 에러가 안나고 very fast라는 말이 출력되게 오버라이딩.
class bird:
    def fly(self):
        raise NotImplementedError
class eagle(bird):
    def fly(self):
        print('very fast')
eagle = eagle()
eagle.fly()
#이처럼 오버라이딩을 해야 에러가 발생하지 않음.

#문제10. 이름을 입력하면 월급을 출력하는 함수를 만드는데 월급이 3000이상인 사원들은 해당 사원의 월급을 볼 수 없습니다. 라는 에러를 발생
import pandas as pd
def find_sal():
    name = input('이름? : ')
    emp = pd.read_csv(r'D:\data\emp_comm.csv')
    result = emp[['sal']][emp['ename'] == name].values[0][0]
    if result >= 3000:
        raise Exception('해당 사원의 월급 못봄!')
    else:
        return result

find_sal()

#문제11. MIT TTT함수 중 1부터 9사이 숫자를 받게해서 해당 숫자를 출력하는 함수를 생성하는데 1부터 9사이가 아니면 잘못 입력하셨습니다. 라는 에러 메시지가 나오게 하는 합수
def get_num():
    num = int(input('# : '))
    if num <1 or num >10:
        raise Exception('숫자를 잘못 입력함..')
    else:
        return num

get_num()

#문제12. 위 코드를 수정해서 1~9까지 숫자를 입력하지 않으면 숫자를 다시 물어보게
def get_num():
    num=0
    while (num <1) or (num>9):
        num = int(input('# : '))
    if num <1 or num >10:
        raise Exception('숫자를 잘못 입력함..')
    else:
        return num

get_num()

#문제13. 머신러닝화 하지 않은 ttt를 수행해서 숫자를 1~9번 외의 번호를 입력

import random
from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player
    # 착수
    def action(self, state):
        printboard(state)
        action = None
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        while action not in range(1, 10):
            try :
                action = int(input('Your move? '))
            except ValueError:
                continue
        return switch_map[action]


    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))
def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner
if __name__ == "__main__":
    p1 = Human(1)
    p2 = Human(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)


#문제14. 입력안해도 다시물어보게끔.
def get_number():
    num = ''
    while num not in range(1,10):
        try :
            num=int(input('숫자를 입력하세요'))
        except ValueError:
            continue
    return num

get_number()







