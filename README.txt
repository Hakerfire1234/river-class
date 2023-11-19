# MyRiver

MyRiver is a Python class that represents a simple river-like data structure.

## Features

- Add elements to the river.
- Change the value of an element at a specified index.
- Block elements from a specified index onwards.
- Check if the river is empty.

## Usage

1. **Initialize MyRiver:**
    ```python
    river_manager = myriver()
    ```

2. **Add Elements:**
    ```python
    for _ in range(10):
        river_manager.add_stream()
    ```

3. **Change Element Value:**
    ```python
    river_manager.flow(1, 5)
    ```

4. **Block Elements:**
    ```python
    river_manager.block_stream(4)
    ```

5. **Check if River is Empty:**
    ```python
    is_empty = river_manager.is_empty()
    ```

## Methods

### `add_stream()`

Adds a new element to the river.

### `flow(index: int, key: Any)`

Changes the value of an element at the specified index.

### `block_stream(index: int)`

Blocks elements from the specified index onwards.

### `is_empty() -> bool`

Returns `True` if the river is empty, `False` otherwise.

### `current_state() -> List[Any]`

Returns the current state of the river.
