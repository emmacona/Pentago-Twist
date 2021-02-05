# Modified code from : Stathis P.
# Source : https://github.com/speix/8-puzzle-solver/blob/36b10ff3eab68d26d29f9a4c38db497a899e1eca/driver.py#L201

from collections import deque
from node import Node
from heapq import heappush, heappop, heapify
import itertools

board_size = 6
board_side = 3
SUCCESS = True
FAIL = False


def sort_tuple(tup):
    return(sorted(tup, key=lambda x: x[1]))


def expand(node, queue):
    index = node.state.index(0)
    moves = []

    if index >= 3: moves.append(Node(up(node.state, index), node, node.depth + 1))
    if index < 3: moves.append(Node(down(node.state, index), node, node.depth + 1))
    if index % 3 > 0:  moves.append(Node(left(node.state, index), node, node.depth + 1))
    if index % 3 < 2: moves.append(Node(right(node.state, index), node, node.depth + 1))

    neighbors = []

    for m in moves:
        if not m.state in queue: 
            neighbors.append(m)

    return neighbors

def up(state, index):
  new_state = state.copy()
  temp = new_state[index - 3]
  new_state[index-3] = new_state[index]
  new_state[index] = temp
  return new_state


def down(state, index):
  new_state = state.copy()
  temp = new_state[index + 3]
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

    explored, queue = [], deque([Node(start_state, None, 0)])

    while queue:
        node = queue.popleft()
        explored.append(node.state)

        if node.state == goal_state:
            return explored

        # find neighbours
        neighbors = expand(node, queue)

        for neighbor in neighbors:
            if neighbor.state not in explored:
                queue.append(neighbor)
                explored.append(neighbor)
    
    return None


# Q1 a) - ii) UCS

# Q1 a) - iii) DFS

# Q1 a) - iv) Iterative deepening


def main():
    initial_state = [1, 4, 2, 5, 3, 0]
    goal_state = [0, 1, 2, 5, 4, 3]

    print("****************************")
    print("BFS")
    path = bfs(initial_state, goal_state)
    print("Number of moves: ", len(path))
    for p in path:
        print(p)


main()
