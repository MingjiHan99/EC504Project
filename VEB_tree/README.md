## VEB Tree Implementation for Ordered Dictionary

This VEB Tree implementation for ordered dictionary supports key-value pairs.

- The `insert` method inserts a new key-value pair into the tree. If the key already exists in the tree, the associated value is updated.
- The `delete` method removes the key-value pair with the given key from the tree.
- The `lookup` method searches for a key-value pair with the given key by traversing the tree.
- The `VEB_max` and `VEB_min` methods find the maxmium and minimum values of the VEB tree and its children.
- The `VEB_successor` method return the next key that exists in the VEB tree.

Again, this implementation assumes that the keys are comparable.

## Usage

To run a Python file, follow these steps:

1. Open a terminal (Command Prompt, PowerShell, or Terminal on macOS/Linux) and navigate to the directory containing the Python file you want to run. For example:

   ```
   cd path/to/your-python-file
   ```

2. Run the Python file using the following command:

   ```
   python3 VEB_Tree.py
   ```