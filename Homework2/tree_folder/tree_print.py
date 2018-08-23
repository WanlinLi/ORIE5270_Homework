class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        """
        get root value
        :return: (double)
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    def get_tree_height(self):
        """
        get tree height
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
        height = self.get_tree_height()
        tree = []
        for i in range(height):
            tree.append(["|"] * (2 ** height - 1))
        matrix = self.print_partial_tree()
        position = []
        for j in range(len(matrix[height - 1])):
            tree[height - 1][2 * j] = matrix[height - 1][j]
            position.append(2 * j)
        for i in range(height - 2, -1, -1):
            new_position = []
            for k in range(len(matrix[i])):
                tree[i][(position[2 * k] + position[2 * k + 1]) / 2] = matrix[i][k]
                new_position.append((position[2 * k] + position[2 * k + 1]) / 2)
            position = new_position
        for i in range(height):
            for j in range(len(tree[0])):
                if tree[i][j] == "None":
                    tree[i][j] = "|"

        return tree

    def print_partial_tree(self):
        """
        print tree without "|"
        :return: list of lists
        """
        height = self.get_tree_height()
        current_lv = [self]
        Matrix = [[str(self.get_value_root())]]
        for k in range(height - 1):
            next_lv = []
            next_lv_value = []
            for i in current_lv:
                if i == "None":
                    next_lv.append("None")
                    next_lv.append("None")
                    next_lv_value.append("None")
                    next_lv_value.append("None")
                else:
                    if i.root:
                        next_lv.append(Tree(i.root.left))
                        next_lv.append(Tree(i.root.right))
                        next_lv_value.append(str(Tree(i.root.left).get_value_root()))
                        next_lv_value.append(str(Tree(i.root.right).get_value_root()))
                    else:
                        next_lv.append("None")
                        next_lv.append("None")
                        next_lv_value.append("None")
                        next_lv_value.append("None")
                current_lv = next_lv
            Matrix.append(next_lv_value)
        return Matrix


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
