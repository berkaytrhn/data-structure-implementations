from typing import Any

class NonLinearNode:
    """
    Simple Node for Graph
    """
    def __init__(self, value) -> None:
        self.value = value
        self.neighbours=list()
        self.distance=float("inf")
        self.parent = None
        
    def add_neighbour(self, neighbour: "NonLinearNode"):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)

    def __repr__(self):
        """Representation method"""
        return f"Node({self.value}), Neighbours: {', '.join(self.neighbours)}"
    
class LinearNode:
    """
    Simple Node for Linear Usage
    """
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next=None
        self.prev=None
        

    def __repr__(self):
        """Representation method"""
        return f"Node: '{self.value}', Next: '{self.next}', Prev: '{self.prev}'"