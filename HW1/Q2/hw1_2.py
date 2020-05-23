# Using a base class to initialize the id of the nodes and the size for the weighted quick union
class UF:
    # referred the documentation for __init__ and self
    def __init__(self, size):
        self.id_no = list(range(size))
        self.sz = list(range(size))


# Class quick find from the base class
# constructor to initialize the class
class QF(UF):

    # for every node, create the id
    def QF(self, n):
        for i in range(0, len(self.id_no), 1):
            self.id_no[i] = i

    # check if the id is same for every node, which means the nodes are connected
    def find(self, p, q):
        return self.id_no[p] == self.id_no[q]

    # if not connected, connect by changing id's of the nodes
    def union(self, p, q):
        id_p = self.id_no[p]
        id_q = self.id_no[q]

        for i in range(0, len(self.id_no), 1):
            if self.id_no[i] == id_p:
                self.id_no[i] = id_q

        return p, q


# class quick union
class QU(UF):
    # similar to quick find, create the id for the nodes
    def QU(self, n):
        for i in range(0, len(self.id_no), 1):
            self.id_no[i] = i

    # find the root for the nodes
    def root(self, i):
        while i != self.id_no[i]:
            i = self.id_no[i]

        return i

    # check if the nodes are connected if the root node is the same
    def find(self, p, q):
        return self.root(p) == self.root(q)

    # if not connected, connect the node by changing the node id to root id
    def union(self, p, q):
        a = self.root(p)
        b = self.root(q)

        self.id_no[a] = b

        return p, q


# class weighted quick union
class WQU(UF):
    # create the id's
    def WQU(self, n):
        for i in range(0, len(self.id_no), 1):
            self.id_no[i] = i

    def root(self, i):
        while i != self.id_no[i]:
            i = self.id_no[i]

        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, lst, p, q):
        a = self.root(p)
        b = self.root(q)

        sz = list(range(len(lst)))
        # use a size data structure to keep track of the height of the trees
        if self.sz[a] < self.sz[b]:
            self.id_no[a] = b
            self.sz[b] += self.sz[a]
        else:
            self.id_no[b] = a
            self.sz[a] += self.sz[b]

        return p, q


def main():
    count1 = count2 = count3 = 0

    # Reading input from the input file
    txt = input("Enter the text file: ")
    txt1 = open(txt, "r")

    # Create an empty list of lists to copy all the data from the text file
    lst = []

    # referred the documentation for the map() method
    # mapping the string elements into an integer
    for l in txt1:
        lst.append(list(map(int, l.split())))

    print("Input data: ", lst)
    print("\n")

    import time

    f = QF(8192)
    print("QUICK FIND")
    start = time.time()
    for [i, j] in lst:
        count1 += 1
        if not f.find(i, j):
            print("The pairs for quick find are: ", f.union(i, j))
    print("Time taken for the quick find algorithm is:", time.time() - start)
    print("\n")

    u = QU(8192)
    print("QUICK UNION")
    start = time.time()
    for [i, j] in lst:
        count2 += 1
        if not u.find(i, j):
            print("The pairs for quick union are: ", u.union(i, j))
            # u.union(lst, i, j)
    print("Time taken for the quick union algorithm is: ", time.time() - start)
    print("\n")

    w = WQU(8192)
    print("WEIGHTED QUICK UNION")
    start = time.time()
    for [i, j] in lst:
        count3 += 1
        if not w.find(i, j):
            print("The pairs for weighted quick union are: ", w.union(lst, i, j))
            # w.union(lst, i, j)
    print("Time taken for the weighted quick union algorithm is: ", time.time() - start)
    print("\n")


if __name__ == '__main__':
    main()
