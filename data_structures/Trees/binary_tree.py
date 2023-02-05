class Node:
    left = None
    right = None
    data = None
    _size = 0 # Specifies the number of nodes in the tree

    def __init__(self, value):
        self.data = value
        self._size += 1
    
    # region - Generic Methods: len(), is_empty(), positions(), iter()
    def __len__(self):
        return self._size
    def is_empty(self):
        return True if (self.data == None) else False
    def positions():
        # TODO
        pass
    def iter():
        # TODO
        pass
    # endregion
    
    def insert(self, value):
        if (value <= self.data):
            # insert left value to insert is <= current node data
            if (self.left == None): # If current node has no left child, give it one with the value to be inserted
                self.left = Node(value)
            else: # Else, tell the left child to insert the value.
                self.left.insert(value)
        else:
            # insert right when value to insert is > the current node data
            if (self.right == None): # If current node has no right child, give it one with the value to be inserted
                self.right = Node(value)
            else: # Else, tell the existing right child to insert the value
                self.right.insert(value)
        self._size += 1
    
    def contains(self, value):
        if (value == self.data):
            return True
        elif (value < self.data and self.left != None):
            self.left.contains(value)
        elif (value > self.data and self.right != None):
            self.right.contains(value)
        else:
            return False
    """
    To traverse inorder, we visit a node after its left tree and before its right tree.
    Left node -> Top node -> Right node
    """
    def printInOrder(self):
        # Start with left
        if (self.left != None):
            self.left.printInOrder()
        # Do the current node
        print(self.data)
        # End with right
        if (self.right != None):
            self.right.printInOrder()
    """
    *May not be accurate*
    To traverse preorder, we visit a child node after its parent nodes.
    Parent node -> Left node -> Right node
    """
    def printPreOrder(self):
        # Start with the current node
        print(self.data)
        # Continue with left
        if (self.left != None):
            self.left.printInOrder()
        # End with right
        if (self.right != None):
            self.right.printInOrder()
    """
    *May not be accurate*
    To traverse postorder, we visit a child node before its parent nodes.
    Left node -> Right node -> Parent node
    """
    def printPostOrder(self):
        # Start with left
        if (self.left != None):
            self.left.printInOrder()
        # Continue with right
        if (self.right != None):
            self.right.printInOrder()
        # End with the current node
        print(self.data)


if __name__ == "__main__":
    node = Node(1)
    node.insert(2)
    node.insert(4)
    node.insert(6)
    node.insert(5)
    node.insert(8)
    node.insert(3)
    # Check pre- and post-order traversals. 
    node.printPostOrder()