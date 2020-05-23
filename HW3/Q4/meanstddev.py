# Average internal path length of a binary search tree (BST)


# Define the Binary Search Tree class which has the functionalities to search and insert nodes
# https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533

from random import shuffle
from statistics import stdev


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


def is_red(n):
    return isinstance(n, RedBlackBST.Node) and n.color == RED


def is_black(n):
    return not is_red(n)


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


def internal_path_len(root, height=0):
    """Calculates the internal path length from the root node until the node with the key value passed in
            the function; if tree is empty, length is 0"""

    if root is None:
        return 0
    else:
        return height + internal_path_len(root.left, height + 1) + internal_path_len(root.right, height + 1)


def main():
	# number of trials = 10
    N = 10

	# create a list from 500 to 10,000 with steps of 500, while appending 1 at the beginning
    for n in [1] + list(range(500, 10001, 500)):
        result = []
        for i in range(N):
            rand_insert = list(range(n))
            shuffle(rand_insert)
			
			# create an object of the RedBlackBST class
            rbt = RedBlackBST()

            for j in rand_insert:
                rbt.insert(j)
            result.append(internal_path_len(rbt.root) / n)

        std_dev = stdev(result)
        mean = sum(result) / len(result)

        print("For {} trials and {} insertions, the mean path length is {:.2f} with a standard deviation of {:.2f}"
              .format(N, n, mean, std_dev))


if __name__ == "__main__":
    main()
