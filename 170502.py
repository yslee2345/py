
#문제2 state 리스트 변수에서 숫자 2를 출력하려면?
#문제3. 아래의 printboard함수에 print를 넣어서 디버깅하시오.
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(cells)
    print(*cells) #리스트에서 요소만 추출
    print(BOARD_FORMAT.format(*cells))

printboard(state)

#문제4. 함수의 매개변수로 함수를 사용할 수 있다고 했다.그러므로 printboard에 매개변수로 emptystate()함수를 사용하면 결과가 어떤게 출력되는지?
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

printboard(emptystate())

state=[[2,0,0],
       [1,0,0],
       [2,0,0]]

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

gameover(state)


def action(state):
    action = None
    while action not in range(1, 10):
        action = int(input('Your move? '))
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
    return switch_map[action]

action(state)
#아무것도 입력하지 않으면 계속 물어보게
def action(state):
    action = None
    while action not in range(1, 10):

        try :
            action = int(input('Your move? '))
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

        except ValueError:
            continue

        return switch_map[action]

action(state)


def episode_over(winner):
    if winner == DRAW:
        print('Game over! It was a draw.')
    else:
        print('Game over! Winner: Player {0}'.format(winner))

episode_over(3)

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


#문제
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
            printboard(state)
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            printboard(state)
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        printboard(state)
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        printboard(state)
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
        while action not in range(1, 10):
            action = int(input('Your move? '))
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

