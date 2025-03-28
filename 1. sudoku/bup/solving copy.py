
from sudoku import Sudoku

counter = 0

def solve(puzzle):
    global counter
    counter += 1
    
    if puzzle.solved():
        print(puzzle)
        return True
    
    for a in puzzle.actions():
        puzzle.do_action(a)
        rez = solve(puzzle)
        puzzle.undo_action(a)
        if rez:
            return True
    return False

def solve_mc(puzzle):
    global counter
    counter += 1
    if puzzle.solved():
        print(puzzle)
        return True
    actions = puzzle.actions_min_cell()
    for a in actions:
        puzzle.do_action(a)
        rez = solve_mc(puzzle)
        puzzle.undo_action(a)
        if rez:
            return True
    return False

def solve_cutoff(puzzle):
    global counter
    counter += 1

    if puzzle.solved():
        print(puzzle)
        return True
    actions = puzzle.actions_with_check()
    for a in actions:
        puzzle.do_action(a)
        rez = solve_cutoff(puzzle)
        puzzle.undo_action(a)
        if rez:
            return True
    return False

#sudoku = Sudoku(Sudoku.HARDSTR)
#sudoku = Sudoku(Sudoku.MEDSTR)
#sudoku = Sudoku(Sudoku.EASYSTR)

#counter = 0
#sudoku = Sudoku(Sudoku.HARDSTR)
#solve(sudoku)
#print(counter)

counter = 0
sudoku = Sudoku(Sudoku.HARDSTR)
solve_mc(sudoku)
print(counter)

