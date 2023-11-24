

from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start, target):
        visited = set()
        queue = deque()
        queue.append(start)

        while queue:
            node = queue.popleft()
            if node == target:
                return True
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False

if __name__ == "__main__":
    # Create a graph
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)

    # Search for items
    item1 = 1
    item2 = 4
    item3 = 6  # Item that is absent

    # Perform BFS and check if items are present
    present1 = graph.bfs(1, item1)
    present2 = graph.bfs(1, item2)
    present3 = graph.bfs(1, item3)

    if present1:
        print(f"{item1} is present in the graph.")
    else:
        print(f"{item1} is not present in the graph.")

    if present2:
        print(f"{item2} is present in the graph.")
    else:
        print(f"{item2} is not present in the graph.")

    if present3:
        print(f"{item3} is present in the graph.")
    else:
        print(f"{item3} is not present in the graph.")

    # Create a NetworkX graph
    G = nx.Graph()
    for u, v in graph.graph.items():
        for w in v:
            G.add_edge(u, w)

    # Draw the graph with labels
    pos = nx.spring_layout(G)
    labels = {node: str(node) for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=labels)

    plt.title("Graph Visualization")
    plt.show()