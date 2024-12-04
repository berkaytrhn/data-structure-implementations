from data_structures.utils.node import LinearNode
from typing import Any

class Stack:
    """
    Basic Linked List Based Stack Implementation
    """
    
    def __init__(self) -> None:
        self.top: LinearNode=None
        self.size:int = 0
            
    def push(self, value: Any) -> None:
        node = LinearNode(value)
        node.next=self.top
        self.top=node
        
        # update size 
        self.size+=1
    
    def pop(self) -> LinearNode:
        if self.is_empty():
            print("Stack is empty")
            return None
        
        _node = self.top
        self.top = self.top.next # null check above to avoid NoneType error
        
        # update size
        self.size-=1 
        return _node
    
    def top(self) -> LinearNode:
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top
    
    def is_empty(self) -> bool:
        return self.top is None
    
    def size(self):
        # precalculated size for performance
        return self.size
    
    def display(self):
        """
        Arrow formatted display of linked list
        """
        current = self.top
        while current:
            print(f"{current.value} {'-> ' if (current.next is not None) else ''}", end=" ")
            current=current.next
        print()