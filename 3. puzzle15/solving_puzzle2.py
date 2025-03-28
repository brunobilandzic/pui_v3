
from puzzle import Puzzle

node_cnt = 0

def bidir_bfs(game : Puzzle):
    global node_cnt
    queue = [ game ]
    visited = { game }
    goal = Puzzle(game.goal)
    queue_goal = [ goal ]
    visited_goal = { goal }
    
    while len(queue) > 0 and len(queue_goal) > 0:
        node_cnt += 1
        if node_cnt % 1000 == 0:
            print(node_cnt, len(queue), len(queue_goal))
        # from start
        state = queue.pop(0)
        if state.solved():
            print(state)
            return True
        if state in visited_goal:
            print("match")
            print(state)
            return True
        for a in state.actions():
            child = Puzzle(state.board, state.zero)
            child.do_action(a)
            if child not in visited:
                queue.append(child)
                visited.add(child)
        # from goal
        state = queue_goal.pop(0)
        if state in visited:
            print("match")
            print(state)
            return True        
        for a in state.actions():
            child = Puzzle(state.board, state.zero)
            child.do_action(a)
            if child not in visited_goal:
                queue_goal.append(child)
                visited_goal.add(child)
    return False

from random import seed

seed(42)
game = Puzzle()
#game.shuffle(30)
game.shuffle(35)
#game.shuffle(50)
#game.shuffle(100)
print(game)
bidir_bfs(game)
print(node_cnt)
        