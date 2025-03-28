import copy

V=0
O=1
K=2
B=3

L="LEFT"
R="RIGHT"
B="BOAT"

CROSS="CROSS"
LOAD="LOAD"
UNLOAD="UNLOAD"



class State:
    def __init__(self, v=L, o=L, k=L, b=(L, None)):
        self.entities = {
            V: v,
            O: o,
            K: k
        }
        self.b = b

    def __str__(self):
        return f"V({self.entities[V]}) O({self.entities[O]}) K({self.entities[K]}) B({self.b[0]},{self.b[1]})"
    
    def __eq__(self, other):
        return self.entities == other.entities and self.b == other.b
    
    def all_actions(self):
        actions = [Action(CROSS)]

        bp = self.b[1]
        bs = self.b[0]

        if bp == None:
            for e in self.entities:
                if self.entities[e] == bs:
                    actions.append(Action(LOAD, e))
        else:
            actions.append(Action(UNLOAD))
                    
        return actions
    
    def apply_action(self, action):
        new_state = copy.deepcopy(self)
        if action.type == CROSS:
            new_state.b = (R if self.b[0] == L else L, self.b[1])
        elif action.type == LOAD:
            new_state.entities[action.entity] = B
            new_state.b = (self.b[0], action.entity)
        elif action.type == UNLOAD:
            new_state.entities[self.b[1]] = self.b[0]
            new_state.b = (self.b[0], None)
        return new_state
    
    def is_goal(self):
        return self.entities[V] == R and self.entities[O] == R and self.entities[K] == R and self.b == (R, None)
    
    def is_terminal(self):
        if self.V == R and self.O == R and self.b[0]==L:
            return True
        if self.V == L and self.O == L and self.b[0]==R:
            return True
        
        return False
    
    def next_states(self):
        actions = self.all_actions()
        next_states = []
        for action in actions:
            new_state = self.apply_action(action)
            next_states.append(new_state)
        return next_states

    def __hash__(self):
        return hash(str(self))
class Action:
    def __init__(self, type, entity=None):
        self.type = type
        self.entity = entity
        
    
    def __str__(self):
        action = ""
        action += self.type
        if self.entity is not None:
            action += f"({self.entity})"

        return action
    
def bfs(start):
    print("BFS")
    i = 0
    visited = set()
    queue = [start]
    while len(queue) > 0:
        i += 1
        current = queue.pop(0)
        if current.is_goal():
            print("bfs iterations", i)
            return current
        visited.add(current)
        for next_state in current.next_states():
            if next_state not in visited:
                queue.append(next_state)

    
    return None

def recursive_dfs(current, visited, depth=0):
    if current.is_goal():
        return current
    visited.add(current)
    for next_state in current.next_states():
        if next_state not in visited:
            result = recursive_dfs(next_state, visited, depth+1)
            if result is not None:
                return result
    return None



def main():
    start = State()
    final = bfs(start)
    print(final)

    final = recursive_dfs(start, set())
    print(final)

if __name__ == "__main__":
    main()