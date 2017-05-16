#문제1. MIT 총정리 5번째 코드(스스로 학습하는 컴퓨터끼리 두는 코드)를 수정해서 agent끼리 서로 게임할 때 printboard가 출력되게.
#문제2. 게임할 때도 나오는 확률이 학습할 때도 보드판에 확률이 출력되게
#문제3. 10000번 학습한 agent와 100000번 학습한 agent를 각각 만들어서 사람과 게임을 붙이려면?
import random,csv
from copy import copy, deepcopy

EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']


def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))


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




class Agent(object):
    def __init__(self, player, verbose=False, lossval=0, learning=True): #문제2. vebose를 True로
        self.values = {}
        self.player = player
        self.verbose = verbose
        self.lossval = lossval
        self.learning = learning
        self.epsilon = 0.1
        self.alpha = 0.99
        self.prevstate = None
        self.prevscore = 0
        self.count = 0


    def episode_over(self, winner):
        self.backup(self.winnerval(winner))
        self.prevstate = None
        self.prevscore = 0

    def action(self, state):
        r = random.random()
        if r < self.epsilon:
            move = self.random(state)
            self.log('>>>>>>> Exploratory action: ' + str(move))
        else:
            move = self.greedy(state)
            self.log('>>>>>>> Best action: ' + str(move))
        state[move[0]][move[1]] = self.player
        self.prevstate = self.statetuple(state)
        self.prevscore = self.lookup(state)
        state[move[0]][move[1]] = EMPTY
        #문제1 답 : printboard(state)
        return move

    def random(self, state):
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i, j))
        return random.choice(available)

    def greedy(self, state):
        maxval = -50000
        maxmove = None
        if self.verbose:
            cells = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    state[i][j] = self.player
                    val = self.lookup(state)
                    state[i][j] = EMPTY
                    if val > maxval:
                        maxval = val
                        maxmove = (i, j)
                    if self.verbose:
                        cells.append('{0:.3f}'.format(val).center(6))
                elif self.verbose:
                    cells.append(NAMES[state[i][j]].center(6))
        if self.verbose:
            print(BOARD_FORMAT.format(*cells))
        self.backup(maxval)
        return maxmove

    def backup(self, nextval):
        if self.prevstate != None and self.learning:
            prevval = self.values[self.prevstate]
            self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)
            Fn = open(r"D:\data\test100000.csv", 'a')
            w = csv.writer(Fn, delimiter=',', lineterminator='\n')
            w.writerow([self.prevstate[0][0],
                        self.prevstate[0][1],
                        self.prevstate[0][2],
                        self.prevstate[1][0],
                        self.prevstate[1][1],
                        self.prevstate[1][2],
                        self.prevstate[2][0],
                        self.prevstate[2][1],
                        self.prevstate[2][2],
                        prevval,
                        self.values[self.prevstate],
                        self.player,
                        ])
            Fn.close()


    def lookup(self, state):
        key = self.statetuple(state)
        if not key in self.values:
            self.add(key)
        return self.values[key]

    def add(self, state):
        winner = gameover(state)
        tup = self.statetuple(state)
        self.values[tup] = self.winnerval(winner)

    def winnerval(self, winner):
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.5
        elif winner == DRAW:
            return 0
        else:
            return self.lossval

    def printvalues(self):
        vals = deepcopy(self.values)
        for key in vals:
            state = [list(key[0]), list(key[1]), list(key[2])]
            cells = []
            for i in range(3):
                for j in range(3):
                    if state[i][j] == EMPTY:
                        state[i][j] = self.player
                        cells.append(str(self.lookup(state)).center(3))
                        state[i][j] = EMPTY
                    else:
                        cells.append(NAMES[state[i][j]].center(3))
            print(BOARD_FORMAT.format(*cells))

    def statetuple(self, state):
        return (tuple(state[0]), tuple(state[1]), tuple(state[2]))

    def log(self, s):
        if self.verbose:
            print(s)


class Human(object):
    def __init__(self, player):
        self.player = player

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
    p1 = Agent(1, lossval=-1)
    p2 = Agent(2, lossval=-1)
    p3 = Agent(1, lossval=-1)
    p4 = Agent(2, lossval=-1)

    for i in range(100000):
        if i % 10 == 0:
            print('Game: {0}'.format(i))

        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

    # for i in range(100000):
    #     if i % 10==0:
    #         print('Game : {0}'.format(i))
    #
    #     winner = play(p3,p4)
    #     p3.episode_over(winner)
    #     p4.episode_over(winner)


    while True:
        p2.verbose = True
        p1 = Human(1)
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

    # if select == 'B':
    #     while True:
    #         p4.verbose = True
    #         p3 = Human(1)
    #         winner = play(p3,p4)
    #         p3.episode_over(winner)
    #         p4.episode_over(winner)

im