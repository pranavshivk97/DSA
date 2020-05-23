# Define the Binary Search Tree class which has the functionalities to search and insert nodes
# https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533


class BST(object):
    root = None

    class Node(object):
        """Defining the nodes to point to the left and right subtrees of the BST"""
        left = right = None

        # Define a constructor for objects of the class, with the key and corresponding value
        def __init__(self, k, v):
            self.key = k
            self.val = v

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

# recursive in-order traversal of the BST
def in_order(root, queue):
    if root is None:
        return -1

    in_order(root.left, queue)
    queue.append(root.key)
    in_order(root.right, queue)

# function to compute rank of the BST
def rank(key, root):
    if root is None:
        return 0

    q = []
    in_order(root, q)
    return q.index(key)

# function to calculate select of a given node
def select(key, root):
    q = []
    in_order(root, q)
    return q[key]


def main():
    txt = []
	
	# open the file and copy the values to a list
    file = open("select-data.txt", "r")

    for line in file:
        txt.append(int(line))
    txt1 = sorted(txt)

    bstree = BST()

    for data in txt:
        bstree.insert(data, txt[data])

    print("Rank(7) = {}".format(rank(7, bstree.root)))
    print("Select(7) = {}".format(select(7, bstree.root)))


if __name__ == "__main__":
    main()
