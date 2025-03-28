
STRING_POSITIONS = {
    "V": 0,
    "O": 1,
    "K": 2,
    "B": 3,
}

ENTITIES = STRING_POSITIONS.keys()
POCETNO_STANJE = "VOKB || ----"
KRAJNJE_STANJE = "---- || VOKB"
LEFT = "LEFT"
RIGHT = "RIGHT"




class Stanje:
    def __init__(self, stanje="VOKB || ----", roditelj=None):
        print("stanje", stanje)
        self.stanje = stanje 
        self.roditelj = roditelj 

    def __str__(self):
        return self.stanje
    
    def as_string(self):
        return self.stanje
    
    def build_state(self, lijeva, desna):
        return f"{''.join(lijeva)} || {''.join(desna)}"
    
    def do_action(self, action):
        print("stanje", self.stanje, "action", action)
        lijeva, desna = self.stanje.split(" || ")
        lijeva = [l for l in lijeva]
        desna = [d for d in desna]

        boat_side = LEFT if lijeva[STRING_POSITIONS["B"]] != "-" else RIGHT
        
        
        if action == "prebaci":
            if boat_side == LEFT:
                boat = lijeva[STRING_POSITIONS["B"]]
                lijeva[STRING_POSITIONS["B"]] = "-"
                desna[STRING_POSITIONS["B"]] = boat
            else:
                boat = desna[STRING_POSITIONS["B"]]
                desna[STRING_POSITIONS["B"]] = "-"
                lijeva[STRING_POSITIONS["B"]] = boat
            
            s = self.build_state(lijeva, desna)
            return s
        
        _action = action
        action = action.split(" ")
        ent = action[1]
        action = action[0]

        if action=="ukrcaj":
            if boat_side == LEFT:
                lijeva[STRING_POSITIONS[ent]] = "-"
                lijeva[STRING_POSITIONS["B"]] = ent
            else:
                desna[STRING_POSITIONS[ent]] = "-"
                desna[STRING_POSITIONS["B"]] = ent
            s =  self.build_state(lijeva, desna)
            return s
           
        if action == "iskrcaj":
            if boat_side == LEFT:
                lijeva[STRING_POSITIONS[ent]] = ent
                lijeva[STRING_POSITIONS["B"]] = "B"
            else:
                print(_action)
                desna[STRING_POSITIONS[ent]] = ent
                desna[STRING_POSITIONS["B"]] = "B"
            return self.build_state(lijeva, desna)

    def undo_action(self, action):
        lijeva, desna = self.stanje.split(" || ")
        ent = action.split(" ")[0]
        smjer = action.split(" ")[1]

        lijeva = lijeva.split()
        desna = desna.split()

        if smjer == "desno":
            lijeva[STRING_POSITIONS[ent]] = ent
            desna[STRING_POSITIONS[ent]] = "-"
        else:
            lijeva[STRING_POSITIONS[ent]] = "-"
            desna[STRING_POSITIONS[ent]] = ent
        
        stanje = f"{''.join(lijeva)} || {''.join(desna)}"
        #self.stanje = stanje
        return stanje
    
    def all_actions(self):
        actions = []
        lijeva, desna = self.stanje.split(" || ")
        boat_side = LEFT if lijeva[STRING_POSITIONS["B"]] == "B" or lijeva[STRING_POSITIONS["B"]] in ENTITIES else RIGHT
        print("boat_side", boat_side)
        obala = lijeva if boat_side == LEFT else desna
        
        brod_prazan = obala[STRING_POSITIONS["B"]] == "B"

        if brod_prazan:
            for ent in obala:
                if ent == "-" or ent == "B":
                    continue
                actions.append(f"ukrcaj {ent}")
        else:
            ent = obala[STRING_POSITIONS["B"]]
            actions.append(f"iskrcaj {ent}")
        
        actions.append("prebaci")

        return actions

    def next_states(self):
        all_actions = self.all_actions()
        states = []
        print("all_actions", all_actions)
        for action in all_actions:
            states.append(Stanje(self.do_action(action), self))
        return states

    def is_goal(self):
        return self.stanje == "---- || VOKB"

    def is_terminal(self):
        lijeva, desna = self.stanje.split(" || ")
        if ("V" in lijeva and "O" in lijeva and lijeva[STRING_POSITIONS["B"]] == "-") or ("O" in lijeva and "K" in lijeva and lijeva[STRING_POSITIONS["B"]] == "-"):
            return True
        if ("V" in desna and "O" in desna and desna[STRING_POSITIONS["B"]] == "-") or ("O" in desna and "K" in desna and desna[STRING_POSITIONS["B"]] == "-"):
            return True



def generate(s=Stanje(), visited = set()):
    if s in visited:
        print(f"{s} visited")
        return
    if s.is_terminal():
        print("terminal", s)
        return
    if s.is_goal():
        print("rješenje", s)
        return
    visited.add(s.as_string())
    print(len(visited))
    for next_state in s.next_states():

        print("state", s, "next_state", next_state)
        generate(next_state, visited)
    
    
    

def main():
    generate()

if __name__ == "__main__":
    main()