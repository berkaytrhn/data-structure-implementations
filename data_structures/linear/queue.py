from typing import Any
from data_structures.utils.node import LinearNode

class Queue:
    """
    Simple clas based Queue implementation 
    """

    def __init__(self) -> None:
        self.front: LinearNode = None
        self.rear: LinearNode = None

    def enqueue(self, value: Any) -> None:
        """ Classical enqueue function for queue implementation"""
        node: LinearNode = LinearNode(value)
        if self.rear is None:
            self.front=node
            self.rear=node
        else:
            self.rear.next = node # linking the new node
            self.rear=node # update rear node

    def dequeue(self) -> Any:
        """ Classical dequeue function for queue implementation"""
        if self.front is None:
            print("Can not dequeue from empty Queue")
            return None
        else:
            # return the value itself
            value = self.front
            self.front = self.front.next

            # front become None after dequeue, that was only node; so queue becomes empty
            if self.front is None:
                self.rear=None

            return value

    def empty(self) -> bool:
        """Check whether its empty or not"""
        return self.rear is None and self.front is None
            