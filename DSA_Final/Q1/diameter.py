# Name: Pranav Shivkumar (ps1029)
# Diameter of a Directed Graph


import time
import matplotlib.pyplot as plt
import numpy as np


# class to define the graph functions
class Graph:
    # initialize the graph
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    # function to compute the shortest distance
    def shortest_dist(self, d, spt):
        min_index = 0
        min = float("inf")  # set maximum distance for every vertex from the source to infinity

        # repeatedly update the distances, if not visited
        for v in range(self.vertices):
            if d[v] < min and spt[v] is False:
                min = d[v]
                min_index = v

        return min_index

    # function to run Dijkstra's algorithm
    def dijkstra(self, source):
        dist = [float("inf")] * self.vertices  # set all distances from the source vertex to be infinity
        dist[source] = 0        # set distance from source vertex to be 0
        spt = [False] * self.vertices  # initially all vertices are unvisited, so marked as False

        for i in range(self.vertices):  # recursively compute distance
            u = self.shortest_dist(dist, spt)       # returns the vertex closest to

            spt[u] = True  # once visited, mark as visited or True

            for v in range(self.vertices):  # calculate distance from source
                if self.graph[u][v] > 0 and spt[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        return dist


# function to plot the run-times of the 4 text files
def plot_results(t):
    num = np.array([8, 250, 1000])  # , 10000])

    fig = plt.figure()
    fig.canvas.set_window_title("Runtime Estimation")

    plt.plot(num, t, color="c", marker="o")

    plt.xlabel("Number of Vertices")
    plt.ylabel("Time Taken (ns)")
    plt.title("Runtime Estimation")

    plt.savefig("Runtime_Estimation.png")

    plt.show()


def main():
    # define the files to read
    files = ["tinyEWD.txt", "file2.txt", "file3.txt"]  # , "file4.txt"]
    t = []

    # iterate over the files
    for file in files:
        print("Importing data from ", file, "into the graph...\n")

        file1 = open(file, "r")
        vertices = int(file1.readline())
        g = Graph(vertices)  # create the graph with the vertices

        num_edges = file1.readline()

        # add the edges as defined in the text files
        for line in file1:
            u = int(line.split(" ")[0])
            v = int(line.split(" ")[1])
            w = float(line.split(" ")[2])

            g.graph[u][v] = w

        dist = []
        diameter = 0
        # compute time taken and store in array t
        start = time.time_ns()
        # compute the distance from every vertex to the other
        for i in range(vertices):
            dist.append(g.dijkstra(i))

        # find the maximum among each list to get the diameter
        for j in range(len(dist)):
            diameter = max(dist[j])

        stop = time.time_ns()
        print("For {} vertices, diameter is = {:.2f}".format(vertices, diameter))
        print("Time taken = {}".format(stop - start), "ns.\n")

        t.append(stop - start)

    # function call to plot the results
    plot_results(t)


if __name__ == '__main__':
    main()
