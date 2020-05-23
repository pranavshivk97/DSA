# Percentage of red nodes in a red black tree


class BST(object):
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
            """If the node's key is the key being searched for, return the corresponding value"""
            if self.key == key:
                if self.val is not None:
                    return self.val
                else:
                    return self.key

            """If the key of the node is smaller than the root node's key, traverse the left subtree"""
            if self.key < key:
                self.left.search(key)

            """If the key of the node is greater than the root node's key, traverse the right subtree """
            if self.key > key:
                self.right.search(key)

            """If tree is empty, return None"""
            return None

        # Function to insert a Node to the tree
        def insert(self, key, value):
            """If the key already exists, print the same and return nothing; otherwise, check if it is less than or
            greater than the root node and traverse the left or right subtree respectively"""

            # val = self.search(self.key)

            if self.key == key:
                self.val = value
            elif key < self.key:
                if self.left is None:
                    self.left = self.__class__(key, value)
                else:
                    self.left.insert(key, value)
            else:
                if self.right is None:
                    self.right = self.__class__(key, value)
                else:
                    self.right = self.right.insert(key, value)

            return self

    def search(self, key):
        if self.root is not None:
            return self.root.search(key)
        else:
            return None

    def insert(self, key, val):
        """If tree is empty, add a Node, otherwise insert the node to the root"""
        if self.root is None:
            self.root = self.Node(key, val)
        else:
            self.root.insert(key, val)

# https://github.com/peterhil/leftrb/blob/master/leftrb/llrb.py
# http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
# by Robert Sedgewick of Princeton University.

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
            """if key < self.key:
                self.left = self.left.insert(key, val)
            elif key > self.key:
                self.right = self.right.insert(key, val)
            else:
                self.val = val"""

            if is_red(self.left) and is_red(self.right):
                self.flip_colors()

            self = super(RedBlackBST.Node, self).insert(key, val)

            if is_red(self.right) and is_black(self.left):
                self.rotate_left()
            if is_red(self.left) and is_red(self.left.left):
                self.rotate_right()

            return self

        def size(self):
            return 1 + sum(map(lambda c: c.size(), filter(None, [self.left, self.right])))

    def __len__(self):
        if self.root is None:
            return None
        else:
            return self.root.size()

    def insert(self, key, val=None):
        super(RedBlackBST, self).insert(key, val)
        self.root.color = BLACK


del BST


def in_traverse(root):
    red = 0
    if not root.left or not root.right:
        if is_red(root):
            return 1
        else:
            return 0

    red += in_traverse(root.left)
    if is_red(root):
        red += 1

    red += in_traverse(root.right)

    return red


def percent_red(rbt):
    red = in_traverse(rbt.root)
    count = rbt.__len__()

    return red / count


def main():
	# define number of trials (1)
    N = 1
    import random
	
	# calculate the percentage of red nodes by appending the nodes into the BST
    for m in [10000, 100000, 1000000]:
        print("Calculating percentage.....")
        result = []
        shuff_res = []
        for n in range(N):
            for j in range(m):
                shuff_res.append(random.randint(1, m))
                rbt = RedBlackBST()

                for i in shuff_res:
                    rbt.insert(i)

                result.append(percent_red(rbt))

        print("For 1 trial, the percentage of red nodes in the red black tree with {} random nodes is: {:.2f}%.".format
              (m, 100 * sum(result) / len(result)))


if __name__ == '__main__':
    main()
