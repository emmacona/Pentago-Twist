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


def expand(node, queue):
    index = 0
    a, b, c = [], [], []
    # find 0 in array
    for i in range(6):
        if node.state[i] == 0:
            index = i

    if index == 0:
        # right
        nb1, state1 = right(node.state, index)
        # down
        nb2, state2 = down(node.state, index)
        if (nb1 < nb2):
            a = state1
            b = state2
        else:
            a = state2
            b = state1
    if index == 1:
        # right
        nb1, state1 = right(node.state, index)
        # left
        nb2, state2 = left(node.state, index)
        # down
        nb3, state3 = down(node.state, index)

        if max(nb1, nb2, nb3) == nb1:
            if max(nb2, nb3) == nb2:
                a = state1
                b = state2
                c = state3
            else:
                a = state1
                b = state3
                c = state2
        if max(nb1, nb2, nb3) == nb2:
            if max(nb1, nb3) == nb1:
                a = state2
                b = state1
                c = state3
            else:
                a = state2
                b = state2
                c = state1
        if max(nb1, nb2, nb3) == nb3:
            if max(nb1, nb2) == nb1:
                a = state3
                b = state2
                c = state1
            else:
                a = state3
                b = state2
                c = state1
    if index == 2:
        # left
        nb1, state1 = left(node.state, index)
        # down
        nb2, state2 = down(node.state, index)
        if (nb1 < nb2):
            a = state1
            b = state2
        else:
            a = state2
            b = state1
    if index == 3:
        # right
        nb1, state1 = right(node.state, index)
        # up
        nb2, state2 = up(node.state, index)
        if (nb1 < nb2):
            a = state1
            b = state2
        else:
            a = state2
            b = state1
    if index == 4:
        # right
        nb1, state1 = right(node.state, index)
        # left
        nb2, state2 = left(node.state, index)
        # up
        nb3, state3 = up(node.state, index)

        if max(nb1, nb2, nb3) == nb1:
            if max(nb2, nb3) == nb2:
                a = state1
                b = state2
                c = state3
            else:
                a = state1
                b = state3
                c = state2
        elif max(nb1, nb2, nb3) == nb2:
            if max(nb1, nb3) == nb1:
                a = state2
                b = state1
                c = state3
            else:
                a = state2
                b = state2
                c = state1
        else:
            if max(nb1, nb2) == nb1:
                a = state3
                b = state2
                c = state1
            else:
                a = state3
                b = state2
                c = state1
    if index == 5:
        # left
        nb1, state1 = left(node.state, index)
        # up
        nb2, state2 = up(node.state, index)
        if (nb1 < nb2):
            a = state1
            b = state2
        else:
            a = state2
            b = state1

    queue.append(Node(a, node, node.depth + 1))
    queue.append(Node(b, node, node.depth + 1))
    queue.append(Node(c, node, node.depth + 1))

    return queue


def up(new_state, index):
    temp = new_state[index - 3]
    new_state[index-3] = new_state[index]
    new_state[index] = temp
    return temp, new_state


def down(new_state, index):
    temp = new_state[index + 3]
    new_state[index + board_side] = new_state[index]
    new_state[index] = temp
    return temp, new_state


def left(new_state, index):
    temp = new_state[index - 1]
    new_state[index - 1] = new_state[index]
    new_state[index] = temp
    return temp, new_state


def right(new_state, index):
    temp = new_state[index + 1]
    new_state[index + 1] = new_state[index]
    new_state[index] = temp
    return temp, new_state


def get_neighbors(queue, node):
    neighbors = []
    depth = node.depth
    for n in queue:
        if node.depth == depth:
            neighbors.append(n)
    return neighbors


def bfs(start_state, goal_state):

    global max_frontier_size, max_search_depth

    explored, queue = [], [Node(start_state, None, 0)]

    path = []

    while queue:
      node = queue.pop(0)
      if node.state != []:
        explored.append(node.state)
        print(node.state)

        # add children to queue
        queue = expand(node, queue)

        # find neighbours
        neighbors = get_neighbors(queue, node)

        if node.state == goal_state:
            return path

        for neighbor in neighbors:
            if neighbor.state not in explored:
                queue.append(neighbor)
                explored.append(neighbor)

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
