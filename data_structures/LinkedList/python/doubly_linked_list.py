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
    _top: DoublyNode | None
    _last: DoublyNode | None

    def __init__(self):
        super().__init__()
        self._last = None
    
    """
        TODO: Add a reference to the last element in the list to traverse it in reverse order
    """
    def add(self, value):
        newNode = DoublyNode(value)
        if (isinstance(self._top, DoublyNode)):
            self._top.setPrev(newNode)
        if (self._last == None):
            self._last = self._top
        newNode.setNext(self._top)
        self._top = newNode
        self._size += 1

        # if (self._last == None):
        #     self._last = newNode
        # else:
        #     self._last.setPrev()
            