from itertools import chain, imap

class Node(object):
    """A node of a tree"""
    
    def __init__(self, data=None, parent=None):
        """Create a node with the given data"""
        self.data = data
        self.children = []

        if parent:
            parent.add_child(self)

    def __iter__(self):
        for v in chain(*imap(iter, self.children)):
            yield v
        yield self

    def set_data(self, data):
        self.data = data

    def add_child(self, child):
        self.children.append(child)
