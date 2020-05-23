# Dijkstra's algorithm
# Reference: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def print_shortest_path(self, d):
        print("Vertex\tDistance")
        diameter = d[0]
        for v in range(self.vertices):
            if d[v] > diameter:
                diameter = d[v]
            # print("{}\t\t{:.2f}".format(v, d[v]))
            print("Diameter = ", diameter)

    # function to calculate the shortest distance
    def shortest_dist(self, d, spt):
        min_index = 0
        min = float("inf")      # set max to infinity

        # repeatedly update the distances, if not visited
        for v in range(self.vertices):
            if d[v] < min and spt[v] is False:
                min = d[v]
                min_index = v

        return min_index

    # function to start the algorithm
    def Dijkstra(self, source):
        d = [float("inf")] * self.vertices      # set all distances from the source vertex to be infinity
        d[source] = 0
        spt = [False] * self.vertices       # initially all vertices are unvisited

        for i in range(self.vertices):      # recursively compute distance
            u = self.shortest_dist(d, spt)

            spt[u] = True       # once visited, mark as visited or True

            for v in range(self.vertices):      # calculate distance from source
                if self.graph[u][v] > 0 and spt[v] is False and d[v] > d[u] + self.graph[u][v]:
                    d[v] = d[u] + self.graph[u][v]

        self.print_shortest_path(d)


def main():
    g = Graph(8)

    edges_4b = [
        [4, 5, 0.35],
        [5, 4, 0.35],
        [4, 7, 0.37],
        [5, 7, 0.28],
        [7, 5, 0.28],
        [5, 1, 0.32],
        [0, 4, 0.38],
        [0, 2, 0.26],
        [7, 3, 0.39],
        [1, 3, 0.29],
        [2, 7, 0.34],
        [6, 2, 0.40],
        [3, 6, 0.52],
        [6, 0, 0.58],
        [6, 4, 0.93]
    ]

    for u, v, w in edges_4b:
        g.graph[u][v] = w

    print("Dijkstra's Algorithm Results - Q4b: ")
    for i in range(8):
        print(i, "\n")
        g.Dijkstra(i)
    print("\n")


    # g.Dijkstra(0)


if __name__ == '__main__':
    main()

