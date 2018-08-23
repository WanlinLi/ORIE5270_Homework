class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        """
        Get the value of the root node
        :return: (double)
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    def get_tree_height(self):
        """
        Get the height of the tree
        :return: (int)
        """
        if self.root is None:
            return 0
        else:
            left = Tree(self.root.left)
            right = Tree(self.root.right)
            return 1 + max(left.get_tree_height(), right.get_tree_height())

    def print_tree(self):
        """
        print the tree
        :return: list of lists
        """
        tree_height = self.get_tree_height()
        Matrix = []
        for i in range(tree_height):
            Matrix.append(["|"] * (2 * tree_height - 1))
        left_count = 0
        right_count = 0
        Matrix = self.print_sub_tree(tree_height, Matrix, left_count, right_count)
        return Matrix

    def print_sub_tree(self, tree_height, matrix, left_count, right_count):
        """
        print the tree
        :param tree_height: (int)
        :param matrix: list of lists
        :param left_count: (int)
        :param right_count: (int)
        :return: list of lists
        """
        leaf_height = self.get_tree_height()
        root = self.get_value_root()
        center = tree_height - left_count + right_count - 1
        matrix[tree_height - leaf_height][center] = str(root)
        left = Tree(self.root.left)
        left_value = left.get_value_root()
        right = Tree(self.root.right)
        right_value = right.get_value_root()
        if left_value is not None:
            matrix = left.print_sub_tree(tree_height, matrix, left_count + 1, right_count)
        if right_value is not None:
            matrix = right.print_sub_tree(tree_height, matrix, left_count, right_count + 1)
        return matrix

class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
