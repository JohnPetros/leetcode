from typing import Any

from _node import Node


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self._size = 0
    
    def push(self, value: Any) -> None:
        node = Node(value)
        
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
        if self.first is None:
            self.first = node
            
        self._size += 1
        
        
    def __len__(self) -> int:
        return self._size
                
        
        