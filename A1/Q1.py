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

    if index in [3,4,5]: moves.append((node.state[index-3], Node(up(node.state, index), node, node.depth + 1)))
    if index in [0,1,2]: moves.append((node.state[index+3], Node(down(node.state, index), node, node.depth + 1)))
    if index in [1,2,4,5]:  moves.append((node.state[index-1], Node(left(node.state, index), node, node.depth + 1)))
    if index in [0,1,3,4]: moves.append((node.state[index+1], Node(right(node.state, index), node, node.depth + 1)))

    moves.sort(key=lambda x: x[0])

    neighbors = []

    for m in moves:
        if not m[1].state in queue: 
            neighbors.append(m[1])

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
  new_state[index + 3] = new_state[index]
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
    for p in path:
      print(p)
    print("Number of moves: ", len(path))


main()
