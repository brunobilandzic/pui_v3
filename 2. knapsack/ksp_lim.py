
class KSPBState: # limited number of objects

    Weights = [ 23, 35, 18, 26, 31, 31, 15, 28, 19, 19 ]
    Values = [ 2, 3, 1, 4, 5, 5, 2, 3, 3, 3 ]
    Capacity = 100
    
    def __init__(self, in_sack=[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]):
        self.in_sack = in_sack
        self.weight = sum(self.in_sack[i]*self.Weights[i] for i in range(len(self.Weights)))
    
    def actions(self):
        return  [ i for i in range(len(self.Weights)) if self.weight+self.Weights[i] <= self.Capacity and self.in_sack[i] < 1 ]
    
    def do_action(self, act):
        self.in_sack[act] += 1
        self.weight += self.Weights[act]
        
    def undo_action(self, act):
        self.in_sack[act] -= 1
        self.weight -= self.Weights[act]
    
    def value(self):
        return sum(self.in_sack[i]*self.Values[i] for i in range(len(self.Weights)))

    
def bforce(state: KSPBState):
    global ncnt
    ncnt += 1
    actions = state.actions()    
    if len(actions) == 0:
        return state.value()
    maxv = 0
    for a in actions:
        state.do_action(a)
        v = bforce(state)
        state.undo_action(a)
        if v > maxv:
            maxv = v
    return maxv

bound = 0
def bforce_bound(state: KSPBState):
    global ncnt, bound
    ncnt += 1
    actions = state.actions()    
    if len(actions) == 0:
        v = state.value()
        if v > bound:
            print(state.in_sack, v)
            bound = v
        return bound
    for a in actions:
        state.do_action(a)
        v = bforce_bound(state)
        state.undo_action(a)
        if v > bound:
            bound = v
    return bound

memory = [ [ -1 ] * (KSPBState.Capacity + 1) for _ in range(len(KSPBState.Weights)+1) ]

def dp(state: KSPBState, d: int=0):
    global ncnt
    ncnt += 1

    rc = KSPBState.Capacity - state.weight
    if d >= len(KSPBState.Weights) or rc == 0:
        memory[d][rc] = 0
        return 0

    # don't take dth item
    if memory[d+1][rc] < 0: # lookup failed    
        dp(state, d+1)
    
    # take dth item if legal
    if state.weight + KSPBState.Weights[d] > KSPBState.Capacity:
        memory[d][rc] = memory[d+1][rc]
    else:
        if memory[d+1][rc-KSPBState.Weights[d]] < 0: # lookup failed    
            state.do_action(d)
            dp(state, d+1)
            state.undo_action(d)
        memory[d][rc] = max(memory[d+1][rc], memory[d+1][rc-KSPBState.Weights[d]] + KSPBState.Values[d])
    return memory[d][rc]
            
ksp = KSPBState()
print(ksp.Weights)
print(ksp.Values)
ncnt = 0; print(bforce(ksp), ncnt)
#ncnt = 0;  print(bforce_bound(ksp), ncnt)
ncnt = 0;  print(dp(ksp), ncnt)
#print(memory)
