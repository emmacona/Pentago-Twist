from collections import deque
from node import Node
from heapq import heappush, heappop, heapify
import itertools

initial_state = [1, 4, 2, 5, 3, 0]
goal_state = [0, 1, 2, 3, 4, 5]
SUCCESS = True
FAIL = False


def swap(state, pos1, pos2):
  new_state = state.copy()
  new_state[pos1] = state[pos2]
  new_state[pos2] = state[pos1]
  return new_state


def get_moves(node):
  # [0][1][2]
  # [3][4][5]
  state = node.copy()
  index = 0
  left, right, down, up = index-1, index+1, index+3, index-3  # indices
  a, b, c = [], [], []  # children in order of priority - lowest nb first

  if node == []:
    return [a, b, c]

  for i in range(len(state)):
    if (state[i] == 0):
      index = i
    
  # Legal moves:
  # For index 0: right, down
  if (index == 0):
    if (state[right] >= state[down]):
      a = swap(state, index, down)
      b = swap(state, index, right)
    else:
      a = swap(state, index, right)
      b = swap(state, index, down)

  # For index 1: right, left, down
  if (index == 1):
    opt = [state[right], state[left], state[down]]

    if (state[right] == max(opt)):
      if (state[left] > state[down]):
        a = swap(state, index, down)
        b = swap(state, index, left)
        c = swap(state, index, right)
      else:
        a = swap(state, index, left)
        b = swap(state, index, down)
        c = swap(state, index, right)

    elif (state[left] == max(opt)):
      if (state[right] > state[down]):
        a = swap(state, index, down)
        b = swap(state, index, right)
        c = swap(state, index, left)
      else:
        a = swap(state, index, right)
        b = swap(state, index, down)
        c = swap(state, index, left)
    
    else:
      if (state[right] > state[left]):
        a = swap(state, index, left)
        b = swap(state, index, right)
        c = swap(state, index, down)
      else:
        a = swap(state, index, right)
        b = swap(state, index, left)
        c = swap(state, index, down)

  # For index 2: left, down
  if (index == 2):
    if (state[left] >= state[down]):
      a = swap(state, index, down)
      b = swap(state, index, left)
    else:
      a = swap(state, index, left)
      b = swap(state, index, down)
  
  # For index 3: up, right
  if (index == 3):
    if (state[right] >= state[up]):
      a = swap(state, index, up)
      b = swap(state, index, right)
    else:
      a = swap(state, index, right)
      b = swap(state, index, up)

  # For index 4: left, right, up
  if (index == 4):
    opt = [state[right], state[left], state[up]]

    if (state[right] == max(opt)):
      if (state[left] > state[up]):
        a = swap(state, index, up)
        b = swap(state, index, left)
        c = swap(state, index, right)
      else:
        a = swap(state, index, left)
        b = swap(state, index, up)
        c = swap(state, index, right)
        
    elif (state[left] == max(opt)):
      if (state[right] > state[up]):
        a = swap(state, index, down)
        b = swap(state, index, right)
        c = swap(state, index, left)
      else:
        a = swap(state, index, right)
        b = swap(state, index, up)
        c = swap(state, index, left)
    
    else:
      if (state[right] > state[left]):
        a = swap(state, index, left)
        b = swap(state, index, right)
        c = swap(state, index, up)
      else:
        a = swap(state, index, right)
        b = swap(state, index, left)
        c = swap(state, index, up)

  # For index 5: up, left
  if (index == 5):
    if (state[left] >= state[up]):
      a = swap(state, index, up)
      b = swap(state, index, left)
    else:
      a = swap(state, index, left)

  return [a, b, c]

def get_neighbours(tree, current_node):
  neighbours = []
  # find index of current node
  index = 0
  for node in tree:
    if(node != current_node):
      index += 1
  
  # We have a neighbour to the left
  if (index < 3):
    for i in range(index):
      neighbours.append(tree[i])
  
  if (index > 3):
    neighbours.append(tree[index + 3])

  if (index % 3 == 0):
    neighbours.append(tree[index-1])
  
  if (index % 3 > 0):
    neighbours.append(tree[index+1])
  
  return neighbours
  

# Q1 a) - i) BFS
def bfs(initial_state, goal_state):
  queue = []
  explored = []
  queue.append(initial_state)
  tree = [initial_state]

  while queue:
    current_node = queue.pop(0)
    explored.append(current_node)

    children = get_moves(current_node)

    tree.append(children[0])
    tree.append(children[1])
    tree.append(children[2])

    if (current_node != []):
      queue.append(children[0])
      queue.append(children[1])
      queue.append(children[2])
      print(current_node)
      print('\n')

      if (current_node == goal_state):
        return queue

      neighbours = get_neighbours(queue, current_node)

      for neighbour in neighbours:
        if neighbour not in explored:
          queue.append(neighbour)
          explored.append(neighbour)


# Q1 a) - ii) UCS

# Q1 a) - iii) DFS

# Q1 a) - iv) Iterative deepening


def main():
  initial_state = [1, 4, 2, 5, 3, 0]
  goal_state = [0, 1, 2, 3, 4, 5]

  # Question 1 a)i) BFS
  solution = bfs(initial_state, goal_state)
  while solution:
    state = solution
    print(state)

main()