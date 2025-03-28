from copy import deepcopy

BROD = "B"
LEFT = "L"
RIGHT = "R"
VUK = "V"
OVCA = "O"
KUPUS = "K"

class State():
    def __init__(self, init_str = "VOKB || ----", parent = None, in_boat = None):
        left_str = list(init_str.split(" || ")[0])
        
        right_str = list(init_str.split(" || ")[1])
        self.str = init_str
        self.left = { "V": False, "O": False, "K": False, "B": False }
        self.right = { "V": False, "O": False, "K": False, "B": False }

        for i in range(4):
            if left_str[i] != "-":
                self.left[left_str[i]] = True
            if right_str[i] != "-":
                self.right[right_str[i]] = True

        self.side = LEFT if self.left["B"] else RIGHT
        self.parent = parent
        self.in_boat = in_boat
    
    def __str__(self):
        return self.as_string()
    
    def as_string(self):
        left_str = []
        right_str = []

        for entity in self.left:
            left_str.append(entity if self.left[entity] else "-")
        for entity in self.right:
            right_str.append(entity if self.right[entity] else "-")


        return f"{''.join(left_str)} || {''.join(right_str)}"

    
    def all_actions(self):
        actions = []
        actions.append("prebaci brod")
        if self.in_boat is not None:
            actions.append(f"iskrcaj {self.in_boat}")
        else:
            on_shore = self.left.keys() if self.side == LEFT else self.right.keys()
            for entity in on_shore:
                if entity != "B" :
                    actions.append(f"ukrcaj {entity}")

        return actions
    

    def do_action(self, action):
        if action == "prebaci brod":
            if self.side == LEFT:
                self.side = RIGHT
                self.left["B"] = False
                self.right["B"] = True
            else:
                self.side = LEFT
                self.left["B"] = True
                self.right["B"] = False
            return 
        elif action.startswith("iskrcaj"):
            entity = action.split(" ")[1]
            if self.side == LEFT:
                self.left[entity] = True
                # self.right[entity] = False
            else:
                self.right[entity] = True
                #self.left[entity] = False
            self.in_boat = None
            return 
        elif action.startswith("ukrcaj"):
            entity = action.split(" ")[1]
            if self.side == LEFT:
                self.left[entity] = False
            else:
                self.right[entity] = False
            self.in_boat = entity
            return 
        
    def undo_action(self, action):
        if action == "prebaci brod":
            self.side = LEFT if self.side == RIGHT else RIGHT
            return 
        if action.startswith("iskrcaj"):
            entity = action.split(" ")[1]
            if self.side == LEFT:
                self.left[entity] = False
            else:
                self.right[entity] = False
            self.in_boat = entity
            return 
        if action.startswith("ukrcaj"):
            entity = action.split(" ")[1]
            if self.side == LEFT:
                self.left[entity] = True
            else:
                self.right[entity] = True
            self.in_boat = None
            return 
      
    def next_states(self):
        actions = self.all_actions()

        next_states = []
        # new_state = self.copy()
        for action in actions:
            new_state = self.copy()
            new_state.do_action(action)
            new_state.parent = self
            next_states.append(new_state)
        
        return next_states
    
    def is_terminal(self):
        # print(self.left[VUK], self.left[OVCA], self.left[KUPUS], self.left[BROD])
        if self.left[VUK] and self.left[OVCA] and self.side == RIGHT:
            return True
        if self.right[VUK] and self.right[OVCA] and self.side == LEFT:
            return True
        return False
    
    def is_goal(self):
        return self.right[VUK] and self.right[OVCA] and self.right[KUPUS] and self.right[BROD]

    def copy(self):
        return deepcopy(self)

        


    
        

        