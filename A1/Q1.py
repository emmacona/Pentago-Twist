# Modified code from : Stathis P.
# Source : https://github.com/speix/8-puzzle-solver/blob/36b10ff3eab68d26d29f9a4c38db497a899e1eca/driver.py#L201

from collections import deque
from heapq import heappush, heappop, heapify
import itertools

board_size = 6
board_side = 3
SUCCESS = True
FAIL = False
level = 0


def expand(node, queue):

    global level

    index = node.index(0)
    moves = []

    if index in [3,4,5]: moves.append((node[index-board_side], up(node, index)))
    if index in [0,1,2]: moves.append((node[index+board_side], down(node, index)))
    if index in [1,2,4,5]:  moves.append((node[index-1], left(node, index)))
    if index in [0,1,3,4]: moves.append((node[index+1], right(node, index)))

    moves.sort(key=lambda x: x[0])

    neighbors = []

    level += 1

    for m in moves:
        if not m[1] in queue: 
            neighbors.append(m[1])

    return neighbors

def expand_with_level(node_tuple, queue):

    node = node_tuple[1]

    index = node.index(0)
    moves = []

    if index in [3,4,5]: moves.append((node[index-board_side], up(node, index)))
    if index in [0,1,2]: moves.append((node[index+board_side], down(node, index)))
    if index in [1,2,4,5]:  moves.append((node[index-1], left(node, index)))
    if index in [0,1,3,4]: moves.append((node[index+1], right(node, index)))

    moves.sort(key=lambda x: x[0])

    neighbors = []

    for m in moves:
        if not m[1] in queue: 
            neighbors.append((node_tuple[0] + 1, m[1]))

    return neighbors

def up(state, index):
  new_state = state.copy()
  temp = new_state[index - board_side]
  new_state[index-board_side] = new_state[index]
  new_state[index] = temp
  return new_state


def down(state, index):
  new_state = state.copy()
  temp = new_state[index + board_side]
  new_state[index + board_side] = new_state[index]
  new_state[index] = temp
  return new_state


def left(state, index):
  new_state = state.copy()
  temp = new_state[index - 1]
  new_state[index - 1] = new_state[index]
  new_state[index] = temp
  return new_state


def right(state, index):
  new_state = state.copy()
  temp = new_state[index + 1]
  new_state[index + 1] = new_state[index]
  new_state[index] = temp
  return new_state


def bfs(start_state, goal_state):

    global level

    explored, queue = [], deque([(0, start_state)])

    while queue:
        node = queue.popleft()
        explored.append(node[1])

        if node[1] == goal_state:
            return node[0], explored

        # find neighbours
        neighbors = expand_with_level(node, queue)

        for neighbor in neighbors:
            if neighbor[1] not in explored:
                queue.append(neighbor)
                explored.append(neighbor[1])
    
    return 0, None


# Q1 a) - ii) UCS
def uniform_cost(start_state, goal_state):
    # Since the cost are all the same, it will be the same as BFS
    return(bfs(start_state, goal_state))


# Q1 a) - iii) DFS

def dfs(start_state, goal_state):

    explored, queue = [], deque([(0, start_state)])

    while queue:

        node = queue.pop()

        if node[1] == goal_state:
            return node[0], explored

        # find neighbours
        neighbors = expand_with_level(node, queue)
        neighbors.reverse()

        for neighbor in neighbors:
            if neighbor[1] not in explored:
                queue.append(neighbor)
                explored.append(neighbor[1])
    
    return 0, None


def depth_limited_search(state, goal, limit):
    explored, queue = [], deque([(0, state)])

    while queue and limit > 0:
        limit -= 1

        node = queue.pop()

        if node[1] == goal:
            return node[0], explored

        # find neighbours
        neighbors = expand_with_level(node, queue)
        neighbors.reverse()

        for neighbor in neighbors:
            if neighbor[1] not in explored:
                queue.append(neighbor)
                explored.append(neighbor[1])
    
    return 0, None



# Q1 a) - iv) Iterative deepening
def iterative_deepening(start_state, goal_state, max_depth):
    bound = 1

    while bound <= max_depth:
        depth, solution = depth_limited_search(start_state, goal_state, bound)
        if (solution != None):
            return depth, solution
        bound += 1
    
    return 0, None


def main():
    initial_state = [1, 4, 2, 5, 3, 0]
    goal_state = [0, 1, 2, 5, 4, 3]

    print("****************************")
    print("Breadth first search")
    depth, path = bfs(initial_state, goal_state)
    for p in path:
      print(p)
    print("Number of states explored: ", len(path))
    print("Solution path length: ", depth)

    print("\n****************************")
    print("Uniform Cost Search")
    depth, path = bfs(initial_state, goal_state)
    for p in path:
      print(p)
    print("Number of states explored: ", len(path))
    print("Solution path length: ", depth)

    print("\n****************************")
    print("Depth first search")
    depth, path = dfs(initial_state, goal_state)
    for p in path:
      print(p)
    print("Number of states explored: ", len(path))
    print("Solution path length: ", depth)

    print("\n****************************")
    print("Iterative deepening search")
    depth, path = iterative_deepening(initial_state, goal_state, 300)
    if path == None: 
        print("Solution not found in", 300, "levels")
    else:
        for p in path:
            print(p)
        print("Number of states explored: ", len(path))
        print("Solution path length: ", depth)

main()
