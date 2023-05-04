import time




class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 0
        
        
class AVLTree():
    def __init__(self, sleep_time = 0):
        self.root = None
        self.sleep_time = sleep_time
    
    def height(self, node): # height of node
        if node is None:
            return -1
        else:
            return node.height

    def R_rotate(self, node): # LL case
        tmp_tree = node.left
        node.left = tmp_tree.right
        tmp_tree.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        tmp_tree.height = max(self.height(tmp_tree.left), node.height) + 1
        return tmp_tree

    def L_rotate(self, node): # RR case
        tmp_tree = node.right
        node.right = tmp_tree.left
        tmp_tree.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        tmp_tree.height = max(self.height(tmp_tree.right), node.height) + 1
        return tmp_tree

    def RL_rotate(self, node): # RL case
        node.right = self.R_rotate(node.right)
        return self.L_rotate(node)

    def LR_rotate(self, node): # LR case
        node.left = self.L_rotate(node.left)
        return self.R_rotate(node)
    
    def insert(self, key): # insert
        if not self.root: # empty
            self.root = Node(key)
        else:
            self.root = self._insert(key, self.root)
            
    def _insert(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.value:
            time.sleep(self.sleep_time)
            node.left = self._insert(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.value:
                    node = self.R_rotate(node)
                else:
                    node = self.LR_rotate(node)
        elif key > node.value:
            time.sleep(self.sleep_time)
            node.right = self._insert(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.value:
                    node = self.L_rotate(node)
                else:
                    node = self.RL_rotate(node)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node
    
    def find(self, key):
        if not self.root:
            return None
        else:
            return self._find(key, self.root)
    def _find(self, key, node):
        if not node:
            return None
        elif key < node.value:
            return self._find(key, node.left)
        elif key > node.value:
            return self._find(key, node.right)
        else:
            return node
    def _findMin(self, node): # get min value
        if node.left:
            return self._findMin(node.left)
        else:
            return node
    def _findMax(self, node): # get max value
        if node.right:
            return self._findMax(node.right)
        else:
            return node
    
    def delete(self, key, node):
        node = self.root
        if node is None:
            raise KeyError('Key not found.')
        elif key < node.value:
            node.left = self._delete(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.L_rotate(node)
                else:
                    node = self.RL_rotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif key > node.value:
            node.right = self._delete(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.R_rotate(node)
                else:
                    node = self.LR_rotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self._delete(node.key, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self._delete(node.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        return node
    
    
    












