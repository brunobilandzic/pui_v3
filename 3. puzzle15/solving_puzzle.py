
from puzzle import Puzzle

node_cnt = 0

def brute_force(game : Puzzle, d):
    global node_cnt
    node_cnt += 1
    #if node_cnt % 1000 == 0:
    #    print(node_cnt)
    if game.solved():
        print(game)
        return True
    if d == 0:
        return False
    for a in game.actions():
        game.do_action(a)
        r = brute_force(game, d-1)
        game.undo_action(a)
        if r:
            #print(a)
            return True
    return False

def bfs_no_visited(game : Puzzle):
    global node_cnt
    queue = [ game ]
    while len(queue) > 0:
        node_cnt += 1
        #if node_cnt % 1000 == 0:
        #    print(node_cnt)
        state = queue.pop(0)
        if state.solved():
            print(state)
            return True
        for a in state.actions():
            state.do_action(a)
            child = Puzzle(state.board, state.zero)
            queue.append(child)
            state.undo_action(a)
    return False

def bfs_visited(game : Puzzle):
    global node_cnt
    queue = [ game ]
    visited = { game }
    while len(queue) > 0:
        node_cnt += 1
        #if node_cnt % 1000 == 0:
        #    print(node_cnt)
        state = queue.pop(0)
        if state.solved():
            print(state)
            return True
        for a in state.actions():
            state.do_action(a)
            child = Puzzle(state.board, state.zero)
            if child not in visited:
                queue.append(child)
                visited.add(child)
            state.undo_action(a)
    return False

import heapq 

def heuristic(game : Puzzle):
    return sum(1 if g != s else 0 for g, s in zip(game.goal, game.board)) #/ 1000

#def heuristic(game : Puzzle):
#    return sum(abs(g % 4 - s % 4) + abs(g // 4 - s // 4) for g, s in zip(game.goal, game.board)) / 1000

# def heuristic(game : Puzzle):
#     weights = [
#         0, 1, 1, 1,
#         1, 1, 1, 1,
#         10, 10, 10, 10,
#         100, 100, 100, 100,
#         ]
#     return sum(weights[s] / 1000 * (abs(g % 4 - s % 4) + abs(g // 4 - s // 4)) for g, s in zip(game.goal, game.board))

def bestfs(game : Puzzle):
    global node_cnt
    queue = []
    dummy = 0
    heaps = 1
    heapq.heappush(queue, (heuristic(game), dummy, game))
    dummy += 1
    visited = { game }
    besth, bests = float('inf'), None
    while len(queue) > 0:
        node_cnt += 1
        heaps -= 1
        h, _, state = heapq.heappop(queue)
        if h < besth:
            besth, bests = h, state
        #if node_cnt % 3000 == 0:
        #    print(node_cnt, besth, heaps, len(visited))
        #    print(bests)
        if state.solved():
            print(state)
            return True
        for a in state.actions():
            child = Puzzle(state.board, state.zero)
            child.do_action(a)
            if child not in visited:
                heapq.heappush(queue, (heuristic(child), dummy, child))
                heaps += 1
                dummy += 1
                visited.add(child)
    return False

# score(s) = g(s) + h(s)

def astarish(game : Puzzle):
    global node_cnt
    queue = []
    dummy = 0
    heapq.heappush(queue, (heuristic(game) + 0, heuristic(game), 0, dummy, game))
    dummy += 1
    heaps = 1
    visited = { game }
    besth, bests = float('inf'), None
    while len(queue) > 0:
        node_cnt += 1
        gps, h, g, _, state = heapq.heappop(queue)
        heaps -= 1
        if h < besth:
            besth, bests = h, state
        #if node_cnt % 3000 == 0:
        #    print(node_cnt, besth, heaps)
        #    print(bests)
        if state.solved():
            print(state)
            #print(g)
            return True
        for a in state.actions():
            state.do_action(a)
            child = Puzzle(state.board, state.zero)
            if child not in visited:
                heapq.heappush(queue, (heuristic(child)+g+1, heuristic(child), g+1, dummy, child))
                dummy += 1
                heaps += 1
                visited.add(child)
            state.undo_action(a)
    return False


# game = Puzzle(4, [
#     5, 9, 7, 11,
#     2, 10, 3, 15, 
#     1, 6, 14, 13, 
#     4, 8, 12, 0 ])
from random import seed

seed(42)
game = Puzzle()
game.shuffle(30)
#game.shuffle(35)
#game.shuffle(50)
#game.shuffle(100)
print(game)
#print(heuristic(game))

print("BF/DFS")
node_cnt = 0
brute_force(game, 15)
print(node_cnt)

print("BFS")
node_cnt = 0
bfs_no_visited(game)
print(node_cnt)

print("BFSv")
node_cnt = 0
bfs_visited(game)
print(node_cnt)

print("BestFS")
node_cnt = 0
bestfs(game)
print(node_cnt)

print("A*")
node_cnt = 0
astarish(game)
print(node_cnt)
        




