# graph.py

class Graph:
    def __init__(self):
        # Dictionary to store node positions: {'A': (x, y), 'B': (x, y)}
        self.nodes = {}
        # Adjacency list for edges: {'A': {'B': weight}, 'B': {'A': weight}}
        self.edges = {}

    def add_node(self, node_id, pos):
        """Adds a new node to the graph."""
        if node_id not in self.nodes:
            self.nodes[node_id] = pos
            self.edges[node_id] = {}

    def add_edge(self, node1, node2, weight):
        """Adds an undirected edge between two nodes."""
        if node1 in self.nodes and node2 in self.nodes:
            self.edges[node1][node2] = weight
            self.edges[node2][node1] = weight

    def get_adjacency_list(self):
        """Returns the adjacency list for use in algorithms."""
        return self.edges