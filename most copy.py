import copy

V="V"
O="O"
K="K"

ENTITIES = [V, O, K]
EMPTY = "-"

L="LEFT"
R="RIGHT"
B="BOAT"

CROSS="CROSS"
LOAD="LOAD"
UNLOAD="UNLOAD"

PROF_POS = {
    "V": 0,
    "O": 1,
    "K": 2,
    "B": 3,
    "I": 4
}

def build_entities(state_key):
    els = state_key.split(" ")

    entities = {}

    for el in els:
        symbol = el[0]
        
        parenthesis = el.split("(")
        parenthesis = parenthesis[1].split(")")[0]
        print(parenthesis)
        if symbol == "B":
            parenthesis = parenthesis.split(",")
            entities[symbol] = (parenthesis[0], parenthesis[1])
        else:
            entities[symbol] = parenthesis
    return entities
    
    
class State:
    def __init__(self, v=L, o=L, k=L, b=(L, None), parent=None):
        self.entities = {
            V: v,
            O: o,
            K: k
        }
        self.b = b
        self.parent = parent

    def prof_key(self):
        left = ["-"]*5
        right = ["-"]*5

        for entity in self.entities:
            pos = PROF_POS[entity]
            side = self.entities[entity]
            if side == L:
                left[pos] = entity
            elif side == R:
                right[pos] = entity

        if self.b[0] == L:
            left[PROF_POS["B"]] = "B"
        elif self.b[0] == R:
            right[PROF_POS["B"]] = "B"

    
        in_boat = self.b[1]

        if in_boat is not None:
            if self.b[0] == L:
                left[PROF_POS["I"]] = in_boat
            elif self.b[0] == R:
                right[PROF_POS["I"]] = in_boat
        left = "".join(left)
        right = "".join(right)

        return f"{left} || {right}"


    def __str__(self):
        return f"V({self.entities[V]}) O({self.entities[O]}) K({self.entities[K]}) B({self.b[0]},{self.b[1]})"
    
    def as_string(self):
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
        new_state.parent = self
        return new_state
    
    def unapply_action(self, action):
        new_state = copy.deepcopy(self)
        if action.type == CROSS:
            new_state.b = (L if self.b[0] == R else R, self.b[1])
        elif action.type == LOAD:
            new_state.entities[action.entity] = self.b[0]
            new_state.b = (self.b[0], None)
        elif action.type == UNLOAD:
            new_state.entities[self.b[1]] = B
            new_state.b = (self.b[0], self.b[1])
        return new_state
    
    def is_goal(self):
        return self.entities[V] == R and self.entities[O] == R and self.entities[K] == R and self.b == (R, None)
    
    def is_terminal(self):
        if self.entities[V] == R and self.entities[O] == R and self.b[0]==L:
            return True
        if self.entities[V] == L and self.entities[O] == L and self.b[0]==R:
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
    
    def right_side(self):
        on_right = 0
        for entity in self.entities:
            if self.entities[entity] == R:
                on_right += 1
        return on_right
    

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
    i = 0
    visited = set()
    queue = [start]
    while len(queue) > 0:
        i += 1
        current = queue.pop(0)
        if current.is_goal():
            print(f"bfs visited {len(visited)} states, iterations {i}\n")
            path = get_path(current)
            return path
        visited.add(current)
        for next_state in current.next_states():
            if next_state not in visited:
                queue.append(next_state)

    # for state in visited:
    #     print(state)

    

    
    return None

def recursive_bfs(current, visited, depth=0):
    if current.is_goal():
        print(f"recursive bfs, visited {len(visited)} states\n")
        return current
    visited.add(current)
    for next_state in current.next_states():
        if next_state not in visited:
            result = recursive_bfs(next_state, visited, depth+1)
            if result is not None:
                return result
    
    return None

def dfs(start):
    i = 0
    visited = set()
    stack = [start]
    while len(stack) > 0:
        i += 1
        current = stack.pop()
        if current.is_goal():
            print(f"dfs visited {len(visited)} states, iterations {i}\n")
            path = get_path(current)
            return path
        visited.add(current)
        for next_state in current.next_states():
            if next_state not in visited:
                stack.append(next_state)

    return None

def recursive_dfs(current, visited, depth=0):
    if current.is_goal():
        print(f"recursive dfs, visited {len(visited)} states\n")
        return current
    visited.add(current)
    for next_state in current.next_states():
        if next_state not in visited:
            result = recursive_dfs(next_state, visited, depth+1)
            if result is not None:
                return result
    
    return None

def bfs_path(start):
    i = 0
    visited = set()
    queue = [start]
    path = []

    while len(queue) > 0:
        i += 1
        current = queue.pop(0)
        path.append(current)
        if current.is_goal():
            print(f"bfs visited {len(visited)} states, iterations {i}\n")
            return current, path
        
        visited.add(current)
        for next_state in current.next_states():
            if next_state not in visited:
                queue.append(next_state)
        


def generate_dict(current, dictionary={}):
    if current.as_string() in dictionary:
        return 

    dictionary[current.as_string()] = current

    if current.is_goal():
        print(f"generate w/ dict, there are {len(dictionary)} states\n")
        path = get_path(current)
        # for state in path:
        #     print(state)
        return current

    for next_state in current.next_states():
        generate_dict(next_state, dictionary)
        
    
def get_path(current):
    path = []
    while current is not None:
        path.append(current)
        current = current.parent
    return list(reversed(path))

def best_first_search(start):
    i = 0
    visited = set()
    queue = [start]
    while len(queue) > 0:
        i += 1
        current = queue.pop(0)
        if current.is_goal():
            print(f"heuristic visited {len(visited)} states, iterations {i}\n")
            path = get_path(current)
            return path
        visited.add(current)
        next_states = current.next_states()
        next_states.sort(key=lambda x: x.right_side())
        for next_state in next_states:
            if next_state not in visited:
                queue.append(next_state)

def main():
    start = State()
    recursive_bfs(start, set())
    bfs_path = bfs(start)
    
    print("bfs path took visiting", len(bfs_path), "states")
    print()
    for state in bfs_path:
        print(state.prof_key())
    print()
    

    dfs_path = dfs(start)
    
    print("dfs path took visiting", len(dfs_path), "states")
    print()
    for state in dfs_path:
        print(state.prof_key())
    print()

    recursive_dfs(start, set())

    generate_dict(start)

    path = best_first_search(start)
    print("best first search pathtook visiting", len(path), "states")
    print()
    for state in path:
        print(state.prof_key())
    print()


if __name__ == "__main__":
    main()