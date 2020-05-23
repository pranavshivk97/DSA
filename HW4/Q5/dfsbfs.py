import sys
sys.setrecursionlimit(1000000)
# Reference: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Reference: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=rp


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Recursive function for DFS
    def DFS_recurse(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] is False:
                self.DFS_recurse(i, visited)

    # Initial call for DFS
    def DFS(self, v):
        visited = [False] * (len(self.graph))   # set all vertices to unvisited initially

        self.DFS_recurse(v, visited)    # start the algorithm

    # function for BFS
    def BFS(self, s):
        visited = [False] * (len(self.graph))   # set all vertices to unvisited initially

        queue = [s]     # create a queue

        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for i in self.graph[s]:
                if visited[s] is False:
                    queue.append(i)
                    visited[i] = True


def main():
    file = open("NYC.txt", "r")
    num_vertices = int(file.readline())

    g = Graph(num_vertices)

    num_edges = file.readline()

    for line in file:
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = int(line.split(" ")[2])

        g.add_edge(u, v)

        g.DFS(1)
        print("\n")

        g.BFS(1)
        print("\n")


if __name__ == '__main__':
    main()