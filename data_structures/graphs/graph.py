class Node:
    """
    Simple Node for Graph
    """
    def __init__(self, value) -> None:
        self.value = value
        self.neighbours=list()
        self.distance = float("inf")
        self.parent = None
        
    def add_neighbour(self, neighbour: "Node"):
        self.neighbours.append(neighbour)

    def __repr__(self):
        """Representation method"""
        return f"Node({self.value}), Neighbours: {', '.join(self.neighbours)}"

class Graph:
    
    root: Node=None
    nodes: list = None
    
    def __init__(self, root: Node) -> None:
        self.root=root
        self.nodes=list()
    

    def add_edge(self):
        # traverse and add node 
        pass
    
    def add_node(self, value):
        # traverse
        pass