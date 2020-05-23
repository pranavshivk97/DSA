# Checks for cycles in an undirected graph using depth first search (DFS)
# Reference: https://www.geeksforgeeks.org/detect-cycle-undirected-graph/


class Graph:
    # boolean variable to detect for cycles
    isCyclic = False

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[] for i in range(vertices)]

    # function to add edges to the graph
    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def DFS_recurse(self, v, visited, prev):
        # Mark the current vertex as visited
        visited[v] = True

        # For all the vertices adjacent to v
        for i in self.graph[v]:
            if not visited[v]:  # if the vertex is not visited, recursively check adjacent vertices
                self.DFS_recurse(i, visited, v)
            else:
                self.isCyclic = True

        return self.isCyclic

    def DFS(self):
        # Initialize all vertices as unvisited initially
        visited = [False] * len(self.graph)

        for i in range(len(self.graph)):
            if not visited[i]:
                self.DFS_recurse(i, visited, -1)    # recursively visit vertex i and its adjacent vertices
            else:
                self.isCyclic = True    # if visited and parent of i, cycle exists

        return self.isCyclic


def main():
    file = open("graph.txt", "r")
    num_vertices = int(file.readline())
    num_edges = int(file.readline())

    # Create the graph using the number of vertices
    g = Graph(num_vertices)

    # Add the corresponding edges in the graph, specified in the text file
    for line in file:
        i = int(line.split(" ")[0])
        j = int(line.split(" ")[1])
        # k = float(line.split(" ")[2])

        g.add_edge(i, j)

    file.close()

    # Run DFS to detect cycles in the graph
    result = g.DFS()

    if result:
        final_result = "Yes"
    else:
        final_result = "No"

    print("Does the graph have cycles?\n{}".format(final_result))


if __name__ == '__main__':
    main()
