class Node:
    def __init__(self, value):
        self._data = value
        self._next = None
    
    def getNext(self):
        return self._next
    def getData(self):
        return self._data

    def setNext(self, nextNode):
        self.__checkIsValidNode(nextNode)
        self._next = nextNode
    def setData(self, value):
        self._data = value

    def __checkIsValidNode(self, value):
        if value == None:
            return # When the first node is being added, the _top value in the LinkedList is none
        validNode = isinstance(value, Node)
        if not validNode:
            raise Exception("[InvalidNode]: Next value must be an instance of Node class")

            
class LinkedList:
    def __init__(self):
        self._top = None
        self._size = 0 # Number of nodes in the list
    # Adds to the beginning of the linked list
    def add(self, value):
        newNode = Node(value)
        newNode.setNext(self._top)
        self._top = newNode
        self._size += 1
    
    def append(self, value): # similar to the add method obove it, but adds a node to the end of the linked list
        currentNode = self._top

        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
        newNode = Node(value)
        currentNode.setNext(newNode)
        self._size += 1

    def insert(self, value, index):
        currentNode = self._top
        indexCounter = 0

        nodeAtIndex = None
        prevNodeAtIndex = None

        while currentNode != None:
            if indexCounter == index:
                nodeAtIndex = currentNode
                break

            indexCounter += 1
            prevNodeAtIndex = currentNode
            currentNode = currentNode.getNext()
        
        if nodeAtIndex == None:
            print("No node found at index", index) # no node exists at the index argumnent passed in
            return
        
        newNode = Node(value)
        prevNodeAtIndex.setNext(newNode)
        newNode.setNext(nodeAtIndex)
        self._size += 1


    def remove(self, value):
        currentNode = self._top
        previousNode = None

        # Removes the top node if it equals the value to be removed
        willRemoveTopNode = currentNode.getData() == value 
        if willRemoveTopNode:
            self._top = currentNode.getNext()
            self._size -= 1
            return
        
        while currentNode != None:
            if currentNode.getData() == value:
                previousNode.setNext(currentNode.getNext())
                self._size -= 1
                return
            previousNode = currentNode
            currentNode = currentNode.getNext()


    def search(self, value: int):
        currentNode = self._top
        
        while currentNode != None:
            if currentNode.getData() == value:
                return True
            currentNode = currentNode.getNext()
        
        return False

    def printList(self):
        currentNode = self._top
        print("List: ", end="")

        while currentNode != None:
            nodeValue = currentNode.getData()
            print(nodeValue, end=" ")
            currentNode = currentNode.getNext()
        print()
    
    # Can also use the __len__ method
    def getSize(self):
        print("Size: ", self._size)
    
    def __iter__(self):
        self.__currentNode = self._top
        return self
    def __next__(self):
        firstLoop = True
        if self.__currentNode == None:
            raise StopIteration
        
        topNodeData = self.__currentNode.getData()
        self.__currentNode = self.__currentNode.getNext()
        if firstLoop:
            firstLoop = False
            return topNodeData

        return self.__currentNode.getData()

def test_linked_list():
    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(3)
    # linkedList.insert(2.5, 2)

    # While you can use printList...
    linkedList.printList()
    # ...because of the __iter__ and __next__ methods, the linkedList is an iterable
    for node in linkedList:
        print(node)
test_linked_list()

class SortedLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    # add
    def add(self, value):
        currentNode = self._top
        previousNode = None

        # if currentNode == None:
        #     super().add(value)
        #     return

        found = False
        newNode = Node(value)

        while currentNode and not found:
            if currentNode.getData() >= value:
                found = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()
        
        if previousNode:
            previousNode.setNext(newNode)
            newNode.setNext(currentNode)
        else:
            newNode.setNext(self._top)
            self._top = newNode
        
        self._size += 1
    
    def __str__(self):
        return "Sorted Linked List"
    def __repr__(self):
        return self.__str__()

    # insert
    # append

def test_sorted_linked_list():
    sortedLL = LinkedList()
    print(sortedLL)
    # print(sortedLL)
    # sortedLL.add(4)
    # sortedLL.add(9)
    # sortedLL.add(2)
    # sortedLL.add(13)
    # sortedLL.printList()
# test_sorted_linked_list()