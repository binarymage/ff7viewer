import unittest

from ff7viewer import Node

class Test_Node(unittest.TestCase):
    def setUp(self):
        self.tree = Node.Node()

    def test_empty(self):
        """Check that this is an empty tree"""
        self.assertIsNone(self.tree.data)
        self.assertEquals(self.tree.children, [])
        self.assertIsNone(self.tree.parent)

    def test_create_with_data(self):
        """Check that creating with data works"""
        node = Node.Node("aaaa")
        self.assertEquals(node.data, "aaaa")

    def test_create_with_parent(self):
        """Check that creating with a parent works"""
        node = Node.Node("aaaa", self.tree)
        self.assertEquals(node.parent, self.tree)
        self.assertIn(node, self.tree.children)

    def test_set_data(self):
        """Test that data is set okay"""
        self.tree.set_data("aaaa")
        self.assertEquals(self.tree.data, "aaaa")

if __name__ == '__main__':
    unittest.main()
