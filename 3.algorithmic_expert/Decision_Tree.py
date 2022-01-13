# 1. Implement methods to grow a decision tree incrementally. 2. Use these methods to construct a given decision tree. 3. Evaluate this decision tree over multiple sets of signals.

# A decision tree is a data structure that can be evaluated on a set of signals and return a decision (e.g. Yes or No (`"Y"` or `"N"`)). Each interior node of the tree is associated with a particular signal and a constant value against which to compare that signal, and each leaf node has a value which will be returned by the tree. To evaluate the tree on a set of signals we traverse the tree, starting at the root and comparing the appropriate signal value to the constant associated with each interior node. If the signal value is less than the constant we proceed down the left subtree and if it is greater than or equal to the constant we proceed down the right subtree. We continue until we reach a leaf at which point we return the value associated with the leaf.

# For example, suppose that we have a set of integer-valued signals `{X1, X2, X3}`. Consider the following decision tree:

# ```
#            X1 < 3
#         ------------
#        |            |
#     X2 < 1       X1 < 6
#  -----------    ---------
# |           |  |         |
# N           Y  N      X3 < 2
#                     ----------
#                    |          |
#                    Y          N
# ```

# If we evaluate this tree on signals `{X1: 2, X2: 1, X3: 11}` the result will be Y. Evaluating on signals `{X1: 8, X2: 4, X3: 12}` we get N. We can use these to implement decisions that need to be made repeatedly on different input values. For instance, a given decision tree might represent a rule to decide whether or not a given transaction looks fraudulent, and the signals could represent different quantities like `X1`) the age of the account in days, `X2`) the dollar value of the transaction, and `X3`) the time in hours since the last transaction attempt.

# Note: In real life, we would probably grow a decision tree via some machine learning algorithm. In this exercise, however, we will manually create the tree that we want. We can grow a decision tree by starting with a single-leaf tree and recursively splitting the leaves of the tree. We do this by associating a split condition to a node, creating two new leaves below it, and associating a return value to each of those leaves.

# class DecisionTree:
    # add split method
    # add set_leaf_value method
    # add evaluate method

class DecisionTree:
    def __init__(self):
        self.root = None

    def add_split(self, parent, feature, value):
        left = Node(parent, feature, value)
        right = Node(parent, feature, value)
        if parent:
            parent.left = left
            parent.right = right
        return left, right

    def set_leaf_value(self, node, value):
        node.value = value

    def evaluate(self, signals):
        node = self.root
        while node:
            if signals[node.feature] < node.value:
                node = node.left
            else:
                node = node.right
        return node.value if node else None

class Node:
    def __init__(self, parent, feature, value):
        self.parent = parent
        self.feature = feature
        self.value = value
        self.left = None
        self.right = None

    def set_leaf_value(self, value):
        self.value = value

    def evaluate(self, signals):
        if signals[self.feature] < self.value:
            return self.left.evaluate(signals)
        else:
            return self.right.evaluate(signals)


def test_tree():
    dt = DecisionTree()
    left0, right0 = dt.add_split(None, "X1", 3)
    dt.set_leaf_value(right0, False)
    left1, right1 = dt.add_split(left0, "X2", 1)
    dt.set_leaf_value(left1, False)
    dt.set_leaf_value(right1, True)
    print(dt.evaluate({"X1": 4, "X2": 7}))

if __name__ == "__main__":
    test_tree()