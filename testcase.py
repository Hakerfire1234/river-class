from myriver import myriver

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
