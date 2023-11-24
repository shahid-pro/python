

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, source, destination):
        source.neighbors.append(destination)

    def detect_cycle(self):
        visited = set()

        for node in self.nodes:
            if node not in visited:
                if self.is_cyclic(node, visited, None):
                    return True

        return False

    def is_cyclic(self, node, visited, parent):
        visited.add(node)

        for neighbor in node.neighbors:
            if neighbor not in visited:
                if self.is_cyclic(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True

        return False

# Create the graph and add nodes/edges
graph = Graph()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)

graph.add_edge(node1, node2)
graph.add_edge(node2, node3)
graph.add_edge(node3, node4)
#graph.add_edge(node1, node4)


# Detect cycle in the graph
has_cycle = graph.detect_cycle()

if has_cycle:
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")

# Visualize the graph
G = nx.Graph()
for node in graph.nodes:
    G.add_node(node.data)
    for neighbor in node.neighbors:
        G.add_edge(node.data, neighbor.data)

pos = nx.spring_layout(G)
labels = {node.data: str(node.data) for node in graph.nodes}

nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
nx.draw_networkx_labels(G, pos, labels=labels)

plt.title("Graph Visualization")
plt.show()