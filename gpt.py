from copy import deepcopy
from collections import deque

class Stanje:
    def __init__(self, stanje="VOKB || ----", roditelj=None):
        self.stanje = stanje  # Stanje kao string
        self.roditelj = roditelj  # Roditelj stanja za rekonstrukciju puta

    def __str__(self):
        return self.stanje

    def as_string(self):
        return self.stanje

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
            for obj in lijeva.replace("B", ""):
                akcije.append(f"prebaci {obj}")
        else:
            akcije.append("prelazak")
            for obj in desna.replace("B", ""):
                akcije.append(f"prebaci {obj}")
        return akcije

    def next_states(self):
        moguca_stanja = []
        for akcija in self.all_actions():
            novo_stanje = self.copy()
            novo_stanje.action(akcija)
            if not novo_stanje.is_terminal():
                moguca_stanja.append(novo_stanje)
        return moguca_stanja

    def action(self, akcija):
        lijeva, desna = self.stanje.split(" || ")
        if akcija == "prelazak":
            if "B" in lijeva:
                self.stanje = lijeva.replace("B", "") + " || " + desna + "B"
            else:
                self.stanje = lijeva + "B || " + desna.replace("B", "")
        else:
            obj = akcija.split(" ")[1]
            if "B" in lijeva:
                self.stanje = lijeva.replace(obj, "").replace("B", "") + " || " + desna + obj + "B"
            else:
                self.stanje = lijeva + obj + "B || " + desna.replace(obj, "").replace("B", "")

    def undo_action(self, prethodno_stanje):
        self.stanje = prethodno_stanje.stanje

    def copy(self):
        return deepcopy(self)


def generate():
    pocetno = Stanje()
    rjecnik_stanja = {pocetno.as_string(): pocetno}
    stack = [pocetno]

    while stack:
        trenutno = stack.pop()
        for novo in trenutno.next_states():
            if novo.as_string() not in rjecnik_stanja:
                rjecnik_stanja[novo.as_string()] = novo
                stack.append(novo)
    return rjecnik_stanja


def solution_dfs():
    stack = [Stanje()]
    posjeceni = {}
    while stack:
        trenutno = stack.pop()
        if trenutno.is_solved():
            return rekonstrukcija_puta(trenutno)
        posjeceni[trenutno.as_string()] = trenutno
        for novo in trenutno.next_states():
            if novo.as_string() not in posjeceni:
                novo.roditelj = trenutno
                stack.append(novo)
    return None


def solution_bfs():
    queue = deque([Stanje()])
    posjeceni = {}
    while queue:
        trenutno = queue.popleft()
        if trenutno.is_solved():
            return rekonstrukcija_puta(trenutno)
        posjeceni[trenutno.as_string()] = trenutno
        for novo in trenutno.next_states():
            if novo.as_string() not in posjeceni:
                novo.roditelj = trenutno
                queue.append(novo)
    return None


def solution_bestfs():
    pocetno = Stanje()
    queue = [(pocetno, [pocetno])]
    visited = set()
    while queue:
        queue.sort(key=lambda x: sum(1 for obj in x[0].desna if obj in "VOK"), reverse=True)
        stanje, putanja = queue.pop(0)
        if stanje.is_solved():
            return putanja
        visited.add(stanje)
        for akcija in stanje.all_actions():
            novo_stanje = stanje.copy()
            novo_stanje.action(akcija)
            if novo_stanje not in visited and not novo_stanje.is_terminal():
                queue.append((novo_stanje, putanja + [novo_stanje]))
    return []


def rekonstrukcija_puta(stanje):
    putanja = []
    while stanje:
        putanja.append(stanje)
        stanje = stanje.roditelj
    return list(reversed(putanja))

def test():
    print("DFS rješenje:")
    for stanje in solution_dfs():
        print(stanje)
    print("\nBFS rješenje:")
    for stanje in solution_bfs():
        print(stanje)
    print("\nBestFS rješenje:")
    for stanje in solution_bestfs():
        print(stanje)

if __name__ == "__main__":
    test()
