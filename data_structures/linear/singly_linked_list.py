from data_structures.utils.node import LinearNode
from typing import Any

class SinglyLinkedList:
    """
    Basic Implementation of Singly Linked List
    """
    
    def __init__(self) -> None:
        self.head=None
        self.tail=None # keep track of tail for efficiency
        
    
    def add_first(self, data: Any) -> None:
        """
        Add given to beginning
        """
        node = LinearNode(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        
        self.size+=1
        
    
    def add_last(self, data: Any) -> None:
        """
        Add given at the end
        """
        node = LinearNode(data)
        if self.head:
            self.tail.next =node
            self.tail = node
        else:
            self.head = node
            self.tail = node
            
        self.size+=1

    def peek(self, index:int) -> LinearNode:
        """
        Return node at specified index, do not remove just display
        """
        itering_node = self.head
        counter=0
        while itering_node:
            if index == counter:
                return itering_node
            
            itering_node=itering_node.next
            counter+=1
        return None
        
    
    def poll(self) -> LinearNode:
        """
        Remove tail node and return it
        """
        if self.is_empty():
            return None
        
        if self.head == self.tail:
            _node = self.head
            self.clear()
            return _node
            
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        # becomes 1 node prev of tail
        _node = self.tail # next and prev None, alone node to be collected as garbage
        current.next=None
        self.tail=current
        
        self.size-=1
        
        return _node

    def clear(self) -> None:
        """
        Clear out the entire linked list
        """
        self.head=None
        self.tail=None
        self.size=0
    
    def contains(self, data: Any) -> bool:
        """
        Check whether list contains specified data containing node
        """
        current = self.head
        while current:
            if current.value == data:
                return True
            
            current = current.next
            
        return False
    
    def get(self, data: Any) -> LinearNode:
        """
        Get the node at given index
        """
        current = self.head
        while current:
            if current.value == data:
                return current
            current = current.next
            
        return None
    
    
    def is_empty(self) -> bool:
        """
        Return is empty
        """
        return not (self.head and self.tail)
    
    def size(self) -> int:
        """
        Return number of nodes in list
        """
        return self.size
    
    
    def display(self) -> None:
        """
        Arrow formatted display of linked list
        """
        current = self.head
        while current:
            print(f"{current.value} {'-> ' if current != self.tail else ''}", end=" ")
            current=current.next
        print()
        