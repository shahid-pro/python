

import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]

    def min_distance(self, dist, spt_set):
        min_dist = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if (
                    not spt_set[v]
                    and self.graph[u][v] > 0
                    and dist[u] != sys.maxsize
                    and dist[u] + self.graph[u][v] < dist[v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def print_solution(self, dist):
        print("Vertex \t Minimum Distance from Source")
        for node in range(self.V):
            print(f"{node} \t {dist[node]}")

    def visualize_graph(self):
        G = nx.Graph()
        labels = {}
        edge_labels = {}

        for node in range(self.V):
            G.add_node(node)
            labels[node] = str(node)

        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                    G.add_edge(i, j)
                    edge_labels[(i, j)] = str(self.graph[i][j])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_color="black", font_weight="bold")
        nx.draw_networkx_labels(G, pos, labels=labels)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph Visualization")
        plt.show()

# Create a graph
V = 12  # Number of vertices
graph = Graph(V)

# Initialize the graph with edge values (weights)
graph.graph = [
    [0, 4, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
    [4, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 6, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 6, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 10, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
]

# Add self-loops (optional)
for i in range(V):
    graph.graph[i][i] = 0  # Self-loops have a weight of 0

# Connect nodes 7, 8, and 9 to the existing graph with edge values
graph.graph[7][5] = 3
graph.graph[5][7] = 3
graph.graph[8][6] = 4
graph.graph[6][8] = 4
graph.graph[9][3] = 2
graph.graph[3][9] = 2

# Find the minimum distances from source vertex 0
source = 0
shortest_distances = graph.dijkstra(source)
graph.print_solution(shortest_distances)

# Visualize the graph with edge values
graph.visualize_graph()