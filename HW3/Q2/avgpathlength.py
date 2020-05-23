# Average internal path length of a binary search tree (BST)


# Define the Binary Search Tree class which has the functionalities to search and insert nodes
# https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533

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

            val = 0
            val = self.search(self.key)

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
	
	# search function for the tree
    def search(self, key):
        if self.root is not None:
            return self.root.search(key)
        else:
            return None

	# insert function for the tree
    def insert(self, key, val):
        """If tree is empty, add a Node, otherwise insert the node to the root"""
        if self.root is None:
            self.root = self.Node(key, val)
        else:
            self.root.insert(key, val)

# function to recursively calculate the internal path length of the BST
def internal_path_len(root, height=0):
    """Calculates the internal path length from the root node until the node with the key value passed in
            the function; if tree is empty, length is 0"""

    if root is None:
        return 0
    else:
        return height + internal_path_len(root.left, height + 1) + internal_path_len(root.right, height + 1)

# function to plot the graphs as well as the table depicting the results for both cases 
def plot_function(n, data_size, r_res, s_res):
    import matplotlib.pyplot as plt

    cols = ["N-Random Insertions", "N-Sorted Insertions"]
    rows = []
    cell_text = []

    for i in data_size[::10]:
        rows.append(i)

    for pair in zip(r_res[::10], s_res[::10]):
        cell_text.append(["{:.2f}".format(data) for data in pair])

    fig = plt.figure(1)
    ax = fig.add_subplot(111)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, colLabels=cols, rowLabels=rows, loc='center')
    ax.axis('off')

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_size, r_res)
    plt.title("N-Random Insertions")
    plt.xlabel("Data Size")
    plt.ylabel("Average Path Length")

    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_size, s_res)
    plt.title("N-Sorted Insertions")
    plt.xlabel("Data Size")
    plt.ylabel("Average Path Length")

    fig.set_size_inches(w=12, h=10)

    plt.show()


def main():
    from random import shuffle

    n = 100
    rand_insert = []
    sort_insert = []

    r_res = []
    s_res = []

    data_size = range(10, 800, 10)

    for num in data_size:
        rand_avg = []
        sort_avg = []
        for j in range(n):
            sort_insert = list(range(num))
            rand_insert = sort_insert.copy()
            shuffle(rand_insert)
		
		# Create two instances of the BST, one for random inserts, other for sorted inserts
        l1 = BST()
        l2 = BST()

        # Insert the elements in a BST
        for i in rand_insert:
            l1.insert(i, rand_insert[i])

        for k in sort_insert:
            l2.insert(k, sort_insert[k])

        # Calculate the path length
        r_path_length = internal_path_len(l1.root)
        rand_avg.append(r_path_length / num)
        s_path_length = internal_path_len(l2.root)
        sort_avg.append(s_path_length / num)

        # print(r_path_length, "\n", s_path_length)
        r_res.append(sum(rand_avg) / len(rand_avg))
        s_res.append(sum(sort_avg) / len(sort_avg))

    plot_function(n, data_size, r_res, s_res)


if __name__ == "__main__":
    main()
