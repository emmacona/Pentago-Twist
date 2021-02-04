class Node(object):
    def __init__(self, state, parent, depth):

        self.state = state

        self.parent = parent

        self.depth = depth

    def __eq__(self, other):
        return self.state == other
