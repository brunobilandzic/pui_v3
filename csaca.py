
from copy import deepcopy

POSITIONS = {
    "V": 0,
    "O": 1,
    "K": 2,
}

ORDER = ["V", "O", "K", "B"]

visited = []

class Stanje:
    def __init__(self, stanje="VOKB || ----", roditelj=None):
        self.stanje = stanje 
        self.roditelj = roditelj 

    def __str__(self):
        return self.stanje
    
    def as_string(self):
        return self.stanje
    
    def ordered(self):
        lijeva, desna = self.stanje.split(" || ")
        


        return lijeva + " || " + desna

    def is_solved(self):
        return self.stanje == "---- || VOKB"
    
    def is_terminal(self):
        lijeva, desna = self.stanje.split(" || ")
        if "V" in lijeva and "O" in lijeva and "K" in lijeva and "B" in lijeva:
            return False
        if ("V" in lijeva and "O" in lijeva and "B" not in lijeva) or ("O" in lijeva and "K" in lijeva and "B" not in lijeva):
            return True
        if ("V" in desna and "O" in desna and "B" not in desna) or ("O" in desna and "K" in desna and "B" not in desna):
            return True
        return False
    
    def all_actions(self):
        lijeva, desna = self.stanje.split(" || ")
        akcije = []
        if "B" in lijeva:
            akcije.append("prelazak")
            for obj in lijeva.replace("B", "-"):
                akcije.append(f"prebaci {obj}")
        else:
            akcije.append("prelazak")
            for obj in desna.replace("B", "-"):
                akcije.append(f"prebaci {obj}")
        return akcije
    
    def next_states(self):
        moguca_stanja = []
        for akcija in self.all_actions():
            novo_stanje = self.copy().action(akcija)
            
            if not novo_stanje.is_terminal() and novo_stanje.ordered() not in visited:
                visited.append(novo_stanje.ordered())
                moguca_stanja.append(novo_stanje)
        return moguca_stanja
    
    def action(self, akcija):
        lijeva, desna = self.stanje.split(" || ")
        if akcija == "prelazak":
            if "B" in lijeva:
                self.stanje = lijeva.replace("B", "-") + " || " + desna + "B"
            else:
                self.stanje = lijeva + "B || " + desna.replace("B", "-")
        else:
            obj = akcija.split(" ")[1]
            if "B" in lijeva:
                lijeva.replace("B"  , "-")
                lijeva.replace(obj, "-")
                desna = desna[:POSITIONS[obj]] + obj + desna[POSITIONS[obj] + 1:] + "B"
                self.stanje = lijeva + " || " + desna
            else:
                desna.replace("B"  , "-")
                desna.replace(obj, "-")
                lijeva = lijeva[:POSITIONS[obj]] + obj + lijeva[POSITIONS[obj] + 1:] + "B"
                self.stanje = lijeva + " || " + desna
        
        return self

        
    def undo_action(self, prethodno_stanje):
        self.stanje = prethodno_stanje.stanje
    
    def copy(self):
        return deepcopy(self)
    
def generate(stanje):
    print(stanje.stanje)
    if stanje.is_solved():
        return stanje
    if stanje.is_terminal():
        return None
    
    for next_state in stanje.next_states():
        result = generate(next_state)
        if result is not None:
            return result
        
    return None

def main():
    pocetno_stanje = Stanje()
    rjesenje = generate(pocetno_stanje)
    if rjesenje is None:
        print("Nema rjesenja")
    else:
        print("Rjesenje:")
        print(rjesenje.stanje)

if __name__ == "__main__":
    main()
