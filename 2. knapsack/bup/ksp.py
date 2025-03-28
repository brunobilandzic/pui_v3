
class KSPState: # infinite number of objects

    Weights = [ 23, 35, 18, 26, 31, 15, 28, 19 ]
    Values = [ 2, 3, 1, 4, 5, 2, 3, 3 ]
    Capacity = 100
    
    def __init__(self, in_sack=[ 0, 0, 0, 0, 0, 0, 0, 0 ]):
        self.in_sack = in_sack
        self.weight = sum(self.in_sack[i]*self.Weights[i] for i in range(len(self.Weights)))
    
    def actions(self):
        return  [ i for i in range(len(self.Weights)) if self.weight+self.Weights[i] <= self.Capacity ]
    
    def do_action(self, act):
        self.in_sack[act] += 1
        self.weight += self.Weights[act]
        
    def undo_action(self, act):
        self.in_sack[act] -= 1
        self.weight -= self.Weights[act]
    
    def value(self):
        return sum(self.in_sack[i]*self.Values[i] for i in range(len(self.Weights)))

    
def bforce(state: KSPState):
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
def bforce_bound(state: KSPState):
    global ncnt, bound
    ncnt += 1
    actions = state.actions()    
    if len(actions) == 0:
        v = state.value()
        if v > bound:
            #print(state.in_sack, v)
            bound = v
        return bound
    for a in actions:
        state.do_action(a)
        v = bforce_bound(state)
        state.undo_action(a)
        if v > bound:
            bound = v
    return bound

memory = [ 0 ] * (KSPState.Capacity + 1)

def dp(state: KSPState):
    global ncnt
    ncnt += 1

    # lookup
    rc = KSPState.Capacity - state.weight
    if memory[rc] > 0:
        return state.value() + memory[rc]

    actions = state.actions()    
    if len(actions) == 0:
        return state.value()
    else:
        maxv = 0
        for a in actions:
            state.do_action(a)
            v = dp(state)
            state.undo_action(a)
            if v > maxv:
                maxv = v
        # remember
        memory[rc] = maxv - state.value()
        return maxv
        
ksp = KSPState()
ncnt = 0; print(bforce(ksp), ncnt)
ncnt = 0;  print(bforce_bound(ksp), ncnt)
ncnt = 0;  print(dp(ksp), ncnt)
print(memory)

