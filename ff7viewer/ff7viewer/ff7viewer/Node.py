class Node(object):
    """A node of a tree"""
    
    def __init__(self, data=None, parent=None):
        """Create a node with the given data"""
        self.data = data
        self.children = []
        self.parent = parent

        if parent:
            parent.add_child(self)

    def set_data(self, data):
        self.data = data

    def add_child(self, child):
        self.children.append(child)
