## <u>Binary Search Tree Implementation for Ordered Dictionary


This implementation support key-value pairs. 
Each node in the binary search tree contains a key and a value, which are used to store the key-value pairs.

- The ```insert``` method inserts a new key-value pair into the tree. If the key already exists in the tree, the associated value is updated.

- The ```delete``` method removes the key-value pair with the given key from the tree.

- The ```lookup``` method searches for a key-value pair with the given key by traversing the tree in a manner similar to binary search.

- The ```findMin``` and ```deleteMin``` methods are helper methods used in the delete method to handle the case where a node to be deleted has two children.

Again, this implementation assumes that the keys are comparable
