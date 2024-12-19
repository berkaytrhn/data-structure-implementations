from data_structures.utils import LinearNode
from typing import Any

class CircularQueue:
    """
    Linked List based Queue implementation, not fixed size
    """

    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, value: Any) -> None:
        """ Circular enqueue operation"""
        node: LinearNode = LinearNode(value)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node # linking the new node
            self.rear=node # update rear node
            self.rear.next=self.front  # link front node to rear

    def dequeue(self) -> Any:
        """ Circular dequeue operation """
        
        if self.isEmpty():
            print("Can not dequeue from empty Queue")
            return None
        else:
            # return the value itself
            value = self.front
            self.front = self.front.next
            self.rear.next=self.front

            # front become None after dequeue, that was only node; so queue becomes empty
            if self.front is None:
                self.rear=None

            return value

    def isEmpty(self) -> bool:
        """Check whether its empty or not"""
        return self.rear is None and self.front is None

    def display(self):
        """
        Arrow formatted display of circular queue
        """
        current = self.front
        while current:
            print(f"{current.value} {'-> ' if (current.next is not None) else ''}", end=" ")
            current=current.next
            if current==self.front:
                print(f"{current.value}(front)")
                break
        print()
            