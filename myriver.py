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


# Example of using myriver
def example_river_usage():
    river_manager = myriver()

    print("Initial River State:", river_manager.current_state())

    # Add elements to the river
    for _ in range(10):
        river_manager.add_stream()
        print("After Adding Element:", river_manager.current_state())

    # Change the value at index 1
    river_manager.flow(1, 5)
    print("After Changing Element at Index 1:", river_manager.current_state())

    # Block elements from index 4
    river_manager.block_stream(4)
    print("After Blocking Elements from Index 4:",
          river_manager.current_state())

    # Check if the river is empty
    print("Is River Empty?", river_manager.is_empty())


# Run the example
example_river_usage()
