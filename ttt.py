import random
from copy import copy, deepcopy

EMPTY =0
PLAYER_X =1
PLAYER_O =2
DRAW = 3
BOARD_FORMAT = "----------------------------\n" \
               "| {0} | {1} | {2} |\n" \
               "|--------------------------|\n" \
               "| {3} | {4} | {5} |\n" \
               "|--------------------------|\n" \
               "| {6} | {7} | {8} |\n" \
               "----------------------------"
NAMES = ['','X','O']

def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print (BOARD_FORMAT.format(*cells))

def emptystate():
    return [[EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY]]

def gameover(state):
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0]==state[i][1] and state[i][0]==state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i]==state[1][i] and state[0][i]==state[2][i]:
            return state[0][i]
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]

    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW

def last_to_act(state):
    countx = 0
    counto = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == PLAYER_X:
                countx += 1
            elif state[i][j]==PLAYER_O:
                counto += 1
    if countx == counto:
        return PLAYER_O
    if countx == (counto +1):
        return PLAYER_X
    return -1

def enumstates(state,idx,agent):
    if idx>8:
        player = last_to_act(state)
        if player == agent.player:
            agent.add(state)

    else:
        winner = gameover(state)
        if winner != EMPTY:
            return
        i = int(idx/3)
        j = idx % 3
        for val in range(3):
            state[i][j] = val
            enumstates(state,idx+1,agent)

class Agent(object):
    def __init__(self,player,verbose=False,lossval=0,learning=True):
        self.values={}
        self.player = player
        self.verbose = verbose
        self.lossval = lossval
        self.learning = learning
        self.epsilon = 0.1
        self.alpha = 0.99
        self.prevstate = None
        self.prevscore = 0
        self.count = 0
        enumstates(emptystate(),0,self)

    def episode_over(self,winner):
        self.backup(self.winnerval(winner))
        self.prevstate = None
        self.prevscore = 0

    def action(self,state):
        r = random.random()
        if r < self.epsilon:
            move = self.random(state)
            self.log('>>>>>>> Exploratory action : '+str(move))
        else :
            move = self.greedy(state)
            self.log('>>>>>>> Best action :'+str(move))
        state[move[0]][move[1]] = self.player
        self.prevstate = self.statetuple(state)
        self.prevscore = self.lookup(state)
        state[move[0]][move[1]]=EMPTY
        return move

    def random(self,state):
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j]==EMPTY:
                    available.append((i,j))
        return random.choice(available)

    def greedy(self,state):
        maxval = -5000
        maxmove = None
        if self.verbose:
            cells=[]
        for i in range(3):
            for j in range(3):
                if state[i][j]==EMPTY:
                    state[i][j] = self.player
                    val = self.lookup(state)
                    state[]








