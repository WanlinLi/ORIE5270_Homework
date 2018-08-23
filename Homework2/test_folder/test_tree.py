import unittest
from print_tree import Tree
from print_tree import Node


class testtree(unittest.TestCase):
    def test_one_node(self):
        node1 = Node(2, None, None)
        self.tree1 = Tree(node1)
        self.answer1 = ['2']
        assert Tree.print_tree(self.tree1) == self.answer1

    def test_one_branch(self):
        node1 = Node(2, None, None)
        node2 = Node(3, None, None)
        node3 = Node(4, None, None)
        node4 = Node(5, None, None)
        node2.left = node1
        node3.left = node2
        node4.left = node3

        self.tree2 = Tree(node4)
        self.answer2 = [["|", "|", "|", "5", "|", "|", "|"],
                        ["|", "|", "4", "|", "|", "|", "|"],
                        ["|", "3", "|", "|", "|", "|", "|"],
                        ["2", "|", "|", "|", "|", "|", "|"],]

        assert Tree.print_tree(self.tree2) == self.answer2


    def test_full_tree(self):
        node1 = Node(1, None, None)
        node2 = Node(2, None, None)
        node3 = Node(3, None, None)
        node4 = Node(4, None, None)
        node5 = Node(5, None, None)
        node6 = Node(6, None, None)

        node2.left = node4
        node2.right = node5
        node3.right = node6
        node1.left = node2
        node1.right = node3

        self.tree3 = Tree(node1)
        self.answer3 = [["|", "|", "1", "|", "|"],
                        ["|", "2", "|", "3", "|"],
                        ["4", "|", "5", "|", "6"]]

        assert Tree.print_tree(self.tree3) == self.answer3
        
    def test_random_tree(self):
        node1 = Node(1, None, None)
        node2 = Node(2, None, None)
        node3 = Node(3, None, None)
        node4 = Node(4, None, None)
        node5 = Node(5, None, None)
        
        node4.right = node5
        node3.left = node4
        node1.left = node2
        node1.right = node3
        
        self.tree4 = Tree(node1)
        self.answer4 = [["|", "|", "|", "1", "|", "|", "|"],
                        ["|", "|", "2", "|", "3", "|", "|"],
                        ["|", "|", "|", "4", "|", "|", "|"],
                        ["|", "|", "|", "|", "5", "|", "|"],]

        assert Tree.print_tree(self.tree4) == self.answer4
