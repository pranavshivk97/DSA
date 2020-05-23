import time
# Reference: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# Reference: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

# class for Prim's algorithm
class PrimGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    # finds the vertex with minimum distance value from the set of vertices not included in the MST
    def find_min_key(self, key, mst):
        min = float("inf")
        min_index = 0
        for v in range(self.vertices):
            if key[v] < min and mst[v] is False:
                min = key[v]
                min_index = v

        return min_index

    # function used to construct and print the MST using Prim's algorithm
    def Prim(self):
        key = [float("inf")] * self.vertices    # set values of all vertices to infinity
        parent = [None] * self.vertices     # list to store the MST

        key[0] = 0      # initialize vertex to  0 to start the algorithm
        mst = [False] * self.vertices       # boolean array

        parent[0] = -1

        # find the minimum key and add the corresponding endpoint to the mst set
        for v in range(self.vertices):
            u = self.find_min_key(key, mst)
            mst[u] = True

            for w in range(self.vertices):
                if 0 < self.graph[u][w] < key[w] and mst[w] is False:
                    key[w] = self.graph[u][w]
                    parent[w] = u

        # print the constructed mst
        print("Edge\t\tWeight")
        for i in range(1, self.vertices):
            print(parent[i], " - ", i, "\t", self.graph[i][parent[i]])


# class for Kruskal's algorithm
class KruskalGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    # add edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # find set of element
    def find(self, prev, i):
        if prev[i] == i:
            return i
        return self.find(prev, prev[i])

    # computes union of two sets
    def union(self, prev, rank, x, y):
        root_x = self.find(prev, x)
        root_y = self.find(prev, y)

        if rank[root_x] < rank[root_y]:
            prev[root_x] = root_y
        elif rank[root_y] < rank[root_x]:
            prev[root_y] = root_x
        else:
            prev[root_y] = root_x
            rank[root_x] += 1

    # function for Kruskal's algorithm
    def Kruskal(self):
        mst = []    # stores the MST

        i = 0       # index for sorted edges
        j = 0       # index for MST

        # Sort the edges in the non-decreasing order of weights
        self.graph = sorted(self.graph, key=lambda line: line[2])

        prev = []
        rank = []

        # create V subsets with a single element
        for v in range(self.vertices):
            prev.append(v)
            rank.append(0)

        # no of edges to be considered = V-1
        while j < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(prev, u)
            y = self.find(prev, v)

            # if adding the edge doesn't create a cycle add to the MST, else discard it
            if x != y:
                j += 1
                mst.append([u, v, w])
                self.union(prev, rank, x, y)

        # print the MST
        print("Edges\t\tWeight")
        for u, v, w, in mst:
            print("{} - {}\t{}".format(u, v, w))
        print("\n")


def main():
    file = open("graph.txt", "r")
    num_vertices = int(file.readline())
    num_edges = int(file.readline())

    print("PRIM'S ALGORITHM")
    pg = PrimGraph(num_vertices)

    for line in file:
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = float(line.split(" ")[2])

        pg.graph[u][v] = w
        pg.graph[v][u] = w

    file.close()

    start_prim = time.time_ns()
    pg.Prim()
    time_prim = (time.time_ns() - start_prim) / 10**6

    print("KRUSKAL'S ALGORITHM")
    file = open("graph.txt", "r")
    num_vertices = int(file.readline())
    num_edges = int(file.readline())

    kg = KruskalGraph(num_vertices)

    for line in file:
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = float(line.split(" ")[2])

        kg.add_edge(u, v, w)

    file.close()

    start_kruskal = time.time_ns()
    kg.Kruskal()
    time_kruskal = (time.time_ns() - start_kruskal) / 10**6

    print("Time takem by the Prim's algorithm is: {:.2f} ms".format(time_prim))
    print("Time taken by Kruskal's algorithm for the same graph is: {:.2f} ms".format(time_kruskal))


if __name__ == '__main__':
    main()




