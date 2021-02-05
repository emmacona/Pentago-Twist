# Modified code from : Stathis P.
# Source : https://github.com/speix/8-puzzle-solver/blob/36b10ff3eab68d26d29f9a4c38db497a899e1eca/driver.py#L201

from collections import deque
from heapq import heappush, heappop, heapify
import itertools

board_size = 6
board_side = 3
SUCCESS = True
FAIL = False


def expand(node, queue):
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
            neighbors.append(m[1])

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

    explored, queue = [], deque([start_state])

    while queue:
        node = queue.popleft()
        explored.append(node)

        if node == goal_state:
            return explored

        # find neighbours
        neighbors = expand(node, queue)

        for neighbor in neighbors:
            if neighbor not in explored:
                queue.append(neighbor)
                explored.append(neighbor)
    
    return None


# Q1 a) - ii) UCS

# Q1 a) - iii) DFS

def dfs(start_state, goal_state):

    explored, queue = [], deque([start_state])

    while queue:
        node = queue.pop()

        if node == goal_state:
            return explored

        # find neighbours
        neighbors = expand(node, queue)
        neighbors.reverse()

        for neighbor in neighbors:
            if neighbor not in explored:
                queue.append(neighbor)
                explored.append(neighbor)
    
    return None

# Q1 a) - iv) Iterative deepening
def iterative_deepening(start_state, goal_state, iteration):

    explored, queue = [], deque([start_state])

    while queue:
        node = queue.popleft()
        explored.append(node)

        if node == goal_state:
            return explored

        # find neighbours
        neighbors = expand(node, queue)

        for neighbor in neighbors:
            if neighbor not in explored:
                queue.append(neighbor)
                explored.append(neighbor)
    
    return None

def main():
    initial_state = [1, 4, 2, 5, 3, 0]
    goal_state = [0, 1, 2, 5, 4, 3]

    print("****************************")
    print("BFS")
    path = bfs(initial_state, goal_state)
    for p in path:
      print(p)
    print("Number of moves: ", len(path))

    print("****************************")
    print("DFS")
    path = dfs(initial_state, goal_state)
    for p in path:
      print(p)
    print("Number of moves: ", len(path))


main()
