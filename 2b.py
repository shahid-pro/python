import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self):
        self.adjacency_list = []
        self.num_nodes = 0

    def add_edge(self, node1, node2):
        if node1 >= self.num_nodes or node2 >= self.num_nodes:
            print("Error: Invalid node.")
            return

        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def add_vertex(self):
        self.adjacency_list.append([])
        self.num_nodes += 1

    def get_adjacency_matrix(self):
        adjacency_matrix = np.zeros((self.num_nodes, self.num_nodes), dtype=int)

        for node in range(self.num_nodes):
            for neighbor in self.adjacency_list[node]:
                adjacency_matrix[node][neighbor] = 1

        return adjacency_matrix

    def print_graph(self):
        adjacency_matrix = self.get_adjacency_matrix()

        graph = nx.Graph()

        num_nodes = len(adjacency_matrix)

        graph.add_nodes_from(range(num_nodes))

        for i in range(num_nodes):
            for j in range(num_nodes):
                if adjacency_matrix[i][j] == 1:
                    graph.add_edge(i, j)

        nx.draw(graph, with_labels=True)
        plt.show()

# Create a graph with 6 nodes
graph = Graph()

for i in range(6):
    graph.add_vertex()

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 0)

# Print the graph and adjacency matrix
print("Graph with 6 nodes:")
graph.print_graph()
print("Adjacency Matrix:")
print(graph.get_adjacency_matrix())

# Add two extra nodes
graph.add_vertex()
graph.add_vertex()
graph.add_edge(6, 0)
graph.add_edge(6, 1)

# Print the updated graph and adjacency matrix
print("Graph with 8 nodes:")
graph.print_graph()
print("Adjacency Matrix:")
print(graph.get_adjacency_matrix())