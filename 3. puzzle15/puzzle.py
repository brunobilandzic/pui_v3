from random import choice

#  0  1  2  3
#  4  5  6  7
#  8  9 10 11
# 12 13 14 15

class Puzzle(object):
    
    def __init__(self, board=None, zero=None, size=4):
        self.size = size
        if board is not None:
            self.board = board[:]
        else:
            self.board = [ p for p in range(size*size) ]
        if zero is not None:
            self.zero = zero
        else:
            self.zero = self.board.index(0)
        self.goal = [ p for p in range(self.size*self.size) ]
    
    def shuffle(self, diff=1000):
        for _ in range(diff):
            a = choice(self.actions())
            self.do_action(a)

    def __str__(self):
        return '\n'.join(str([ p for p in self.board[i*self.size:(i+1)*self.size] ]) for i in range(self.size))
        
    def actions(self):
        r, c = self.zero // self.size, self.zero % self.size
        acts = []
        if r > 0:
            acts.append((-1, 0))
        if r < self.size-1:
            acts.append((1, 0))
        if c > 0:
            acts.append((0, -1))
        if c < self.size-1:
            acts.append((0, 1))
        return acts
        
    def do_action(self, act):
        dr, dc = act
        nzero = self.zero + (dr * self.size + dc)
        self.board[self.zero], self.board[nzero] = self.board[nzero], self.board[self.zero] 
        self.zero = nzero

    def undo_action(self, act):
        dr, dc = act
        nzero = self.zero - (dr * self.size + dc)
        self.board[self.zero], self.board[nzero] = self.board[nzero], self.board[self.zero] 
        self.zero = nzero

    def solved(self):
        return self.goal == self.board
    
    def __hash__(self):
        return hash(tuple(self.board))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __ne__(self, other):
        return not self.__eq__(other)

if __name__ == '__main__':
    game = Puzzle()
    print(game)