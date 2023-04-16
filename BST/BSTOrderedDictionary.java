public class BSTOrderedDictionary<K extends Comparable<K>, V> {
    private Node root;

    private class Node {
        K key;
        V value;
        Node left, right;

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
            left = right = null;
        }
    }

    public void insert(K key, V value) {
        root = insertNode(root, key, value);
    }

    private Node insertNode(Node node, K key, V value) {
        if (node == null) {
            return new Node(key, value);
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            node.left = insertNode(node.left, key, value);
        } else if (cmp > 0) {
            node.right = insertNode(node.right, key, value);
        } else {
            node.value = value;
        }

        return node;
    }

    public void delete(K key) {
        root = deleteNode(root, key);
    }

    private Node deleteNode(Node node, K key) {
        if (node == null) {
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            node.left = deleteNode(node.left, key);
        } else if (cmp > 0) {
            node.right = deleteNode(node.right, key);
        } else {
            if (node.left == null) {
                return node.right;
            } else if (node.right == null) {
                return node.left;
            } else {
                Node temp = node;
                node = findMin(temp.right);
                node.right = deleteMin(temp.right);
                node.left = temp.left;
            }
        }

        return node;
    }

    public V lookup(K key) {
        Node node = findNode(root, key);
        return node == null ? null : node.value;
    }

    private Node findNode(Node node, K key) {
        if (node == null) {
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            return findNode(node.left, key);
        } else if (cmp > 0) {
            return findNode(node.right, key);
        } else {
            return node;
        }
    }

    private Node findMin(Node node) {
        if (node.left == null) {
            return node;
        } else {
            return findMin(node.left);
        }
    }

    private Node deleteMin(Node node) {
        if (node.left == null) {
            return node.right;
        }

        node.left = deleteMin(node.left);
        return node;
    }

    public static void main(String[] args) {
        BSTOrderedDictionary<Integer, String> dict = new BSTOrderedDictionary<>();

        dict.insert(3, "C");
        dict.insert(1, "A");
        dict.insert(2, "B");
        dict.insert(5, "E");
        dict.insert(4, "D");

        System.out.println("Lookup key 1: " + dict.lookup(1)); // Output: A
        System.out.println("Lookup key 6: " + dict.lookup(6)); // Output: null

        dict.delete(2);
        System.out.println("Lookup key 2: " + dict.lookup(2)); // Output: null
    }
}
