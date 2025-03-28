import copy

ENTITIES = ("V", "O", "K")
EATS = {
    "V": "O",
    "O": "K",
}
STRING_POS = {
    "V", 0,
    "O", 1,
    "K", 2,
}
L = "LEFT"
R = "RIGHT"
B = "BOAT"

CROSS = "CROSS"
LOAD = "LOAD"
UNLOAD = "UNLOAD"

class Entity():
    def __init__(self, symbol, pos=L):
        self.symbol = symbol
        self.pos = pos

    def __str__(self):
        return f"{self.symbol}({self.pos})"
    
class Boat():
    def __init__(self, pos=L, passanger=None):
        self.pos = pos
        self.passanger = passanger
    
    def __str__(self):
        return f"B({self.pos},{self.passanger})"
    
def get_beginning_entites():
    return [Entity(e) for e in ENTITIES]

class Action():
    def __init__(self, type, entity=None):
        self.type = type
        self.entity = entity
        
    
    def __str__(self):
        action = ""
        action += self.type
        if self.entity is not None:
            action += f"({self.entity})"

        return action

class State():
    def __init__(self, entities=get_beginning_entites(), boat=Boat()):
        self.entities = entities
        self.boat = boat
    
    def __str__(self):
        state = ""
        for e in self.entities:
            state += str(e) + " "
        
        state += str(self.boat)
        return state

    def all_actions(self):
        actions = []
        
        actions.append(Action(CROSS))

        passenger = self.boat.passanger
        if passenger is not None:
            actions.append(Action(UNLOAD, passenger))
        else:
            for e in self.entities:
                if e.pos == self.boat.pos:
                    actions.append(Action(LOAD, e))
        
        return actions
    
    def apply_action(self, action):
        if action.type == CROSS:
            self.boat.pos = R if self.boat.pos == L else L
        elif action.type == LOAD:
            self.boat.passanger = action.entity
            action.entity.pos = B
        elif action.type == UNLOAD:
            self.boat.passanger = None
            action.entity.pos = self.boat.pos
        else:
            raise Exception(f"Unknown action: {action}")
    
    def next_states(self):
        actions = self.all_actions()
        next_states = []
        for action in actions:
            new_state = copy.deepcopy(self)
            new_state.apply_action(action)
            next_states.append(new_state)
        return next_states
    
    def is_final(self):
        for e in self.entities:
            if e.pos != R:
                return False
        return True
    
    def is_terminal(self):
        for e in self.entities:
            for e2 in self.entites:
                if e == e2:
                    continue
                if e.pos == e2.pos and EATS[e.symbol] == e2.symbol:
                    return True

        return False


def main():
    state = State()
    print(state)
    all_actions = state.all_actions()
    for a in all_actions:
        print(a)
    for s in state.next_states():
        print(s)

if __name__ == "__main__":
    main()       
            
