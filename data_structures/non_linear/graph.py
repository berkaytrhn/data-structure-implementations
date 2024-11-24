from typing import Dict, Any
from data_structures.utils.node import NonLinearNode


class Graph:
    
    def __init__(self, directed: bool) -> None:
        self.nodes: Dict[Any, NonLinearNode]=dict()
        self.directed=directed

    def add_node(self, value: Any):
        # instead of traversing, we use dict with values as key
        if value not in self.nodes:
            self.nodes[value] = NonLinearNode(value)
        return self.nodes[value]

    def add_edge(self, value1: Any, value2: Any):
        # traverse and add node 
        node1 = self.add_node(value1)
        node2 = self.add_node(value2)
        node1.add_neighbour(node2)
        if not self.directed:
            node2.add_neighbour(node1)
    
    def get_node(self, value: Any) -> NonLinearNode:
        return self.nodes.get(value, None) # if not available, None
    
    
    def display(self):
        for node in self.nodes.values():
            print(f"Node: {node.value}; Neighbours: {', '.join(node.neighbours.__repr__())}")