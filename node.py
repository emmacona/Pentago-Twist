class Node(object):
    def __init__(self, state, depth):

        self.state = state

        self.depth = depth

    def __eq__(self, other):
        return self.state == other