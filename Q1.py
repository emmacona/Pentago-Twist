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
max_search_depth = 0
max_frontier_size = 0

def sort_tuple(tup):  
  return(sorted(tup, key = lambda x: x[1]))   

def expand(node, queue):
    index = 0

    # find 0 in array
    for i in range(6):
      if node.state[i] == 0:
          index = i

    if index == 0:
        # right
        nb1, state1 = right(node.state, index)
        # down
        nb2, state2 = down(node.state, index)

        tup = [(nb1, state1), (nb2, state2)]
        tup = sort_tuple(tup)

    elif index == 1:
        # right
        nb1, state1 = right(node.state, index)
        # left
        nb2, state2 = left(node.state, index)
        # down
        nb3, state3 = down(node.state, index)

        tup = [(nb1, state1), (nb2, state2), (nb3, state3)]
        tup = sort_tuple(tup)

    elif index == 2:
        # left
        nb1, state1 = left(node.state, index)
        # down
        nb2, state2 = down(node.state, index)

        tup = [(nb1, state1), (nb2, state2)]
        tup = sort_tuple(tup)

    elif index == 3:
        # right
        nb1, state1 = right(node.state, index)
        # up
        nb2, state2 = up(node.state, index)
        
        tup = [(nb1, state1), (nb2, state2)]
        tup = sort_tuple(tup)

    elif index == 4:
        # right
        nb1, state1 = right(node.state, index)
        # left
        nb2, state2 = left(node.state, index)
        # up
        nb3, state3 = up(node.state, index)

        tup = [(nb1, state1), (nb2, state2), (nb3, state3)]
        tup = sort_tuple(tup)

    elif index == 5:
      # left
      nb1, state1 = left(node.state, index)
      # up
      nb2, state2 = up(node.state, index)
        
      tup = [(nb1, state1), (nb2, state2)]
      tup = sort_tuple(tup)

    children = [tup[0][1], tup[1][1]]
    if len(tup) > 2:
      children.append(tup[2][1])
    else:
      children.append([])

    queue.append(Node(children[0], node, node.depth+1))
    queue.append(Node(children[1], node, node.depth+1))
    queue.append(Node(children[2], node, node.depth+1))

    return queue

def up(state, index):
  new_state = state.copy()
  temp = new_state[index - 3]
  new_state[index-3] = new_state[index]
  new_state[index] = temp
  return temp, new_state


def down(state, index):
  new_state = state.copy()
  temp = new_state[index + 3]
  new_state[index + board_side] = new_state[index]
  new_state[index] = temp
  return temp, new_state


def left(state, index):
  new_state = state.copy()
  temp = new_state[index - 1]
  new_state[index - 1] = new_state[index]
  new_state[index] = temp
  return temp, new_state


def right(state, index):
  new_state = state.copy()
  temp = new_state[index + 1]
  new_state[index + 1] = new_state[index]
  new_state[index] = temp
  return temp, new_state


def get_neighbors(queue, node):
    neighbors = []
    depth = node.depth
    for n in queue:
        if n.depth == depth and n.state != node.state:
            neighbors.append(n)
    return neighbors


def bfs(start_state, goal_state):

    global max_frontier_size, max_search_depth

    explored, queue = [], [Node(start_state, None, 0)]

    path = []

    while queue:
      node = queue.pop(0)
      if node.state != []:
        print(node.state)

        # add children to queue
        queue = expand(node, queue)

        # find all nodes at this level
        neighbors = get_neighbors(queue, node)

        if node.state == goal_state:
            return path

        for neighbor in neighbors:
            if neighbor.state not in explored:
                queue.append(neighbor)
                explored.append(neighbor.state)

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

        if len(queue) > max_frontier_size:
            max_frontier_size = len(queue)


# Q1 a) - ii) UCS

# Q1 a) - iii) DFS

# Q1 a) - iv) Iterative deepening


def main():
    initial_state = [1, 4, 2, 5, 3, 0]
    goal_state = [0, 1, 2, 3, 4, 5]

    # Question 1 a)i) BFS
    path = bfs(initial_state, goal_state)

    # for state in path:
    #   print(state)


main()
