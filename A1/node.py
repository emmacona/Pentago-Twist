class Node(object):
    def __init__(self, state, parent):
        self.state = state
        self.explored = False
        self.parent = parent
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def explore(self):
        self.explored = True

    def __eq__(self, other):
        return self.state == other

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent
