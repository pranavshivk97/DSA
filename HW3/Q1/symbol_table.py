# Symbol table implementaion using a 2-3 tree as the basis

class BST:
    root = None

    class Node(object):
        """Defining the nodes to point to the left and right subtrees of the BST"""
        left = right = None

        # Define a constructor for objects of the class, with the key and corresponding value
        def __init__(self, k, v):
            self.key = k
            self.val = v

        # Function to search for the node using the key
        def search(self, key):
            if self.key == key:
                return self.val if self.val is not None else self.key

            elif key < self.key and self.left:
                return self.left.search(key)

            elif key > self.key and self.right:
                return self.right.search(key)

            return None

        # Function to insert a Node to the tree
        def insert(self, key, value):
            """If the key already exists, print the same and return nothing; otherwise, check if it is less than or
            greater than the root node and traverse the left or right subtree respectively"""

            if self.key == key:
                self.val = value
            elif key < self.key:
                if self.left is None:
                    self.left = self.__class__(key, value)
                else:
                    self.left = self.left.insert(key, value)
            else:
                if self.right is None:
                    self.right = self.__class__(key, value)
                else:
                    self.right = self.right.insert(key, value)

            return self

    def search(self, key):
        return self.root.search(key) if self.root else None

    def insert(self, key, val):
       self.root = self.Node(key, val) if self.root is None else self.root.insert(key, val)

# https://github.com/peterhil/leftrb/blob/master/leftrb/llrb.py
# http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
# by Robert Sedgewick of Princeton University.

import sys

__all__ = ['RedBlackBST']

RED = True
BLACK = False

# Checks if the node n is red
def is_red(n):
    return isinstance(n, RedBlackBST.Node) and n.color == RED

# Checks if the node n is black
def is_black(n):
    return not is_red(n)

# Implementation of the red-black binary search tree
class RedBlackBST(BST, object):
    root = None

    class Node(BST.Node, object):
        def __init__(self, k, v):
            super(self.__class__, self).__init__(k, v)
            self.color = RED
            self.height = 1

        def rotate_left(self):
            x = self.right
            self.right = x.left
            x.left = self
            x.color = self.color
            self.color = RED

            return x

        def rotate_right(self):
            x = self.left
            self.left = x.right
            x.right = self
            x.color = self.color
            self.color = RED

            return x

        def flip_colors(self):
            self.color = RED
            self.left.color = not self.left.color
            self.right.color = not self.right.color

        def insert(self, key, val=None):
            self = super(RedBlackBST.Node, self).insert(key, val)

            if is_red(self.right) and is_black(self.left):
                self = self.rotate_left()
            if is_red(self.left) and is_red(self.left.left):
                self = self.rotate_right()
            if is_red(self.left) and is_red(self.right):
                self.flip_colors()

            return self

        def move_red_left(self):
            self.flip_colors()

            if self.right and is_red(self.right.left):
                self.right = self.right.rotate_right()
                self = self.rotate_left()
                self.flip_colors()

            return self

        def move_red_right(self):
            self.flip_colors()

            if self.left and is_red(self.left.left):
                self = self.rotate_right()
                self.flip_colors()

            return self

        def delete(self, key):
            assert self.search(key) is not None

            if key < self.key:
                if is_black(self.left) and self.left and is_black(self.left.left):
                    self = self.move_red_left()
                self.left = self.left.delete(key)

            else:
                if is_red(self.left):
                    self = self.rotate_right()

                if key == self.key and self.right is None:
                    return None

                if is_black(self.right) and self.right and is_black(self.right.left):
                    self = self.move_red_right()

                if key == self.key:
                    self.val = self.right.search(self.right.min())
                    self.key = self.right.min()
                    self.right = self.right.delete_min()

                else:
                    self.right = self.right.delete(key)

            return self.fix()

        def delete_min(self):
            if self.left is None:
                return None

            if is_black(self.left) and self.left and is_black(self.left.left):
                self = self.move_red_left()

            self.left = self.left.delete_min()

            return self.fix()

        def delete_max(self):
            if is_red(self.left):
                self = self.rotate_right()

            if self.right is None:
                return None

            if is_black(self.right) and self.right and is_black(self.right.left):
                self = self.move_red_right()

            self.right = self.delete_max()

            return self.fix()

        def fix(self):
            if is_red(self.right):
                self = self.rotate_left()

            if is_red(self.left) and self.left and is_red(self.left.left):
                self = self.rotate_right()

            if is_red(self.left) and is_red(self.right):
                self.flip_colors()

            return self.set_height()

        def set_height(self):
            self.height = 1 + max(self.left and self.left.height or 0, self.right and self.right.height or 0)

            return self

        def size(self):
            return 1 + sum(map(lambda c: c.size(), filter(None, [self.left, self.right])))

    def __len__(self):
        if self.root is None:
            return 0
        else:
            return self.root.size()

    def is_empty(self):
        return self.root is None

    def insert(self, key, val=None):
        super(RedBlackBST, self).insert(key, val)
        self.root.color = BLACK

    def delete(self, key):
        if is_black(self.root.left) and is_black(self.root.right):
            self.root.color = RED

        if self.root is not None:
            self.root = self.root.delete(key)

        if not self.is_empty():
            self.root.color = BLACK

    def delete_max(self):
        self.root = self.root.delete_max()
        self.root.color = BLACK

    def delete_min(self):
        self.root = self.root.delete_min()
        self.root.color = BLACK


del BST

# Implementation of the symbol table API
class SymbolTable:
    tree = RedBlackBST()
    key_iterable = set()

    def put(self, key, value):
        self.tree.insert(key, value)
        self.key_iterable.add(key)

    def get(self, key):
        return self.tree.search(key)

    def delete(self, key):
        self.tree.delete(key)
        self.key_iterable.remove(key)

    def contains(self, key):
        if self.tree.search(key) is not None:
            return True
        else:
            return False

    def is_empty(self):
        if not self.tree.root:
            return True
        else:
            return False

    def size(self):
        return self.tree.root.size()

    def keys(self):
        return self.key_iterable


def main():
	# Define the keys and their corresponding values
    keys = ["A", "S", "S", "I", "G", "N", "M", "E", "N", "T", "T", "H", "R", "E", "E"]
    vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    sym_tb = SymbolTable()

    print("Empty symbol table created!")
    print("is_empty() returns: {}".format(sym_tb.is_empty()))

    print("Adding keys and corresponding values to the table...")

    for i, j in zip(keys, vals):
        sym_tb.put(i, j)
    print("is_empty() = {}".format(sym_tb.is_empty()))
    print("keys() = {}".format(sym_tb.keys()))
    print("size() = {}".format(sym_tb.size()))
    print("contains(T) = {}".format(sym_tb.contains("S")))
    print("delete(A) = {}".format(sym_tb.delete("A")))
    print("keys() = {}".format(sym_tb.keys()))
    print("contains(A) = {}".format(sym_tb.contains("A")))


if __name__ == '__main__':
    main()
