import time

count = 0
count1 = 0
time_radix_ins = []
time_radix_search = []
count_radix_node = []
comp_radix = []
comp_radix1 = []


class RadixNode:
    def __init__(self, k=None):
        """
        Initialize the Node for the radix tree
        """
        self.key = k
        self.children = {}
        self.isLeaf = False

    def leafOrNot(self):
        """
        Check if the node is a leaf or not
        """
        return self.isLeaf

    def __str__(self):
        """
        Specify the string to be returned when the Node is printed
        """
        return self.key


class RadixTree:
    def __init__(self):
        """
        Initialize the radix Tree
        """
        self.root = RadixNode()

    def insert(self, x, k):
        """
        Insert a string at the given node
        """

        if k == '':
            x.isLeaf = True
            return
        combos = getAllStrings(k)
        for a in combos:
            for b in x.children.keys():
                if a[0] == b[:len(a[0])]:


                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        x.children[a[0]].children[b[len(a[0]):]].key = b[len(a[0]):]

                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                            x.children[a[0]].children[a[1][len(a[0]):]].isLeaf = True
                        else:
                            x.children[a[0]].isLeaf = True
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):])
                    return
        x.children[k] = RadixNode(k)
        x.children[k].isLeaf = True

    def count(self, x, string):
        """
        Print the complete sorted tree
        :param x: node at which leaves are searched for
        :param string: contains the string that is formed by parent nodes of x
        :return: None
        """

        global count1
        for a in sorted(x.children.keys()):
            if x.children[a].isLeaf:
                count1+=1
            self.count(x.children[a], string + a)

    def search(self, x, k):
        """
        Search for a string at the given node in the radix treee
        """
        if k == '':
            return x.leafOrNot()
        for a in getAllStrings(k):
            if a[0] in x.children.keys():
                return self.search(x.children[a[0]], k[len(a[0]):])
        return False

    def print_tree(self, x, string, prefix,i):
        """
        Print the complete sorted tree
        """
        global count
        for a in sorted(x.children.keys()):

            if x.children[a].isLeaf:
                if (string + a).startswith(prefix):
                    if i==0:
                        count += 1
                        print(string + a)

            self.print_tree(x.children[a], string + a, prefix,i)

    def spell_checker(self, string):
        """
        Checks is a string exists in the tree
        """
        return self.search(self.root, string)


def getAllStrings(string):
    """
    Yield all string instances from index 0, decreasing string length by 1 at each iteration
    """
    for a in range(len(string), 0, -1):
        yield string[:a], string


def radix_result():
    files = ["no_prefix.txt", "2common_prefix.txt", "3common_prefix.txt", "4common_prefix.txt", "5common_prefix.txt", "6common_prefix.txt"]

    words = [[] for i in range(len(files))]

    for file in range(len(files)):
        print("Importing data from file {}".format(files[file]))
        f = open("words/" + files[file], "r")
        lines = f.readlines()
        for line in lines:
            words[file].append(line.strip())

        R2 = RadixTree()
        start_radix_ins = time.time_ns()

        for i in range(len(words)):
            for word in words[i]:
                R2.insert(R2.root, word)
        stop_radix_ins = time.time_ns()
        time_ins = (stop_radix_ins - start_radix_ins)
        R2.count(R2.root, "")

        print("Number of nodes in the radix tree is = ", count1)



        time_search=0
        string = input('Enter string: ')

        for i in range(1000):
            start_radix_search = time.time_ns()

            R2.print_tree(R2.root, "", string,i)
            if i ==0:
                print("Number of comparisons: ", count)


            time_search += (time.time_ns() - start_radix_search)

        # print("Time taken to insert the words in the radix tree is: ", time_ins, "ns.")

        comp_radix.append(count)
        time_radix_ins.append(time_ins)
        time_radix_search.append(time_search/1000)
        count_radix_node.append(count1)

        print("Comparisons: ", comp_radix)
        print("Insertion times: ", time_radix_ins)
        print("Search times: ", time_radix_search)
        print("Number of Nodes : ", count_radix_node)

        with open("radix_results.txt", "w") as file:
            for item in comp_radix:
                file.write(str(item))
                file.write(" ")
            file.write("\n")
            for item in time_radix_ins:
                file.write(str(item))
                file.write(" ")
            file.write("\n")
            for item in time_radix_search:
                file.write(str(item))
                file.write(" ")
            file.write("\n")
            for item in count_radix_node:
                file.write(str(item))
                file.write(" ")
            file.write("\n")

        file.close()

    return comp_radix, time_radix_ins, time_radix_search, count_radix_node


# def common_prefix():
#     R2 = RadixTree()
#
#     file = open("common_prefix.txt", "r")
#     words = []
#
#     lines = file.readlines()
#     for line in lines:
#         words.append(line.strip())
#
#     for i in range(len(words)):
#         for word in words[i]:
#             R2.insert(R2.root, word)
#
#     string = ["kl", "he", "an", "ne", "mi", "ab", "lo", "ta", "bo", "fl"]
#
#     for s in string:
#         R2.print_tree(R2.root, "", s)
#         print("Number of comparisons: ", count)
#
#         comp_radix1.append(count)
#
#     print("Comparisons: ", comp_radix1)
#
#     with open("common_radix_results.txt", "w") as file:
#         for item in comp_radix1:
#             file.write(str(item))
#             file.write(" ")
#         file.write("\n")
#
#     file.close()
#
#     return comp_radix1
#


