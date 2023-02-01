from linkedlist import Node, LinkedList

class DoublyNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self._prev = None
    
    def getPrev(self):
        return self._prev
    def setPrev(self, value):
        self.__checkIsValidNode(value)
        self._prev = value

class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    # def add(self, value):
    #     newNode = Node(value)
    #     newNode