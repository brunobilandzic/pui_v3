
STRING_POSITIONS = {
    "V": 0,
    "O": 1,
    "K": 2,
    "B": 3
}

ENTITIES = STRING_POSITIONS.keys()
POCETNO_STANJE = "VOKB || ----"
KRAJNJE_STANJE = "---- || VOKB"




class Stanje:
    def __init__(self, stanje="VOKB || ----", roditelj=None):
        self.stanje = stanje 
        self.roditelj = roditelj 

    def __str__(self):
        return self.stanje
    
    def as_string(self):
        return self.stanje
    
    def do_action(self, action):
        lijeva, desna = self.stanje.split(" || ")
        ent = action.split(" ")[0]
        smjer = action.split(" ")[1]

        lijeva = [l for l in lijeva]
        desna = [d for d in desna]

        if smjer == "desno":
            lijeva[STRING_POSITIONS[ent]] = "-"
            desna[STRING_POSITIONS[ent]] = ent
            desna[STRING_POSITIONS["B"]] = "B"
            lijeva[STRING_POSITIONS["B"]] = "-"
        else:
            lijeva[STRING_POSITIONS[ent]] = ent
            desna[STRING_POSITIONS[ent]] = "-"
            lijeva[STRING_POSITIONS["B"]] = "B"
            desna[STRING_POSITIONS["B"]] = "-"

        stanje = f"{''.join(lijeva)} || {''.join(desna)}"
        #self.stanje = stanje
        return stanje

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
        for ent in lijeva:
            if ent == "-":
                continue
            actions.append(f"{ent} desno")
        for ent in desna:
            if ent == "-":
                continue
            actions.append(f"{ent} lijevo")

        return actions

    def next_states(self):
        all_actions = self.all_actions()
        states = []
        for action in all_actions:
            states.append(Stanje(self.do_action(action)))
        return states

    def is_goal(self):
        return self.stanje == "---- || VOKB"

    def is_terminal(self):
        lijeva, desna = self.stanje.split(" || ")
        if ("V" in lijeva and "O" in lijeva and "B" not in lijeva) or ("O" in lijeva and "K" in lijeva and "B" not in lijeva):
            return True
        if ("V" in desna and "O" in desna and "B" not in desna) or ("O" in desna and "K" in desna and "B" not in desna):
            return True

def generate():
    s = Stanje()
    print("počinjem rek")
    visited = set()
    stack = [s]
    i = 0
    while stack:
        i += 1
        current = stack.pop()
        visited.add(current.as_string())
        if current.is_goal():
            print(current, f"broj koraka: {i}")
            return current
        for state in current.next_states():
            if state.as_string() not in visited:
                stack.append(state)

def main():
    generate()

if __name__ == "__main__":
    main() 