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
        adjacency_matrix = [[0] * self.num_nodes for _ in range(self.num_nodes)]

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

# Example usage
graph = Graph()

graph.add_vertex()  # Add node 0
graph.add_vertex()  # Add node 1
graph.add_vertex()  # Add node 2

graph.add_edge(0, 1)  # Add edge between node 0 and node 1
graph.add_edge(1, 2)  # Add edge between node 1 and node 2

graph.print_graph()  # Print the graph using networkx