# Import the myriver class
from typing import Any


class myriver:
    def __init__(self):
        self.river = []

    def flow(self, index: int, key: Any):
        if index > (len(self.river) - 1):
            raise IndexError("River index out of range")
        else:
            self.river[index] = key

    def add_stream(self):
        self.river.append(0)

    def block_stream(self, index: int):
        if index > (len(self.river) - 1):
            raise IndexError("Stream index out of range")
        else:
            del self.river[index+1:]

    def is_empty(self):
        return len(self.river) == 0

    def current_state(self):
        return self.river


