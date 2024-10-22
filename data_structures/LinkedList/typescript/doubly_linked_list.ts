import { LinkedList, Node_ } from "./linkedlist"

class DoublyNode<T> extends Node_<T> {
    private previous: null | DoublyNode<T>;
    constructor(value: T) {
        super(value);
        this.previous = null;
    }
    
    public setPrevious(previousNode: DoublyNode<T>) {
        this.previous = previousNode;
    }

}

class DoublyLinkedList<T> extends LinkedList<T> {
    // protected head: null | DoublyNode<T>;
    // protected tail: null | DoublyNode<T>;

    constructor() {
        super()
        // this.head = this.tail = null;
    }

    public add(nodeValue: T): void {
        const newNode = new DoublyNode<T>(nodeValue);
        if (this.isEmpty()) {
            this.head = this.tail = newNode;
        } else {
            this.tail!.setNext(newNode);
            newNode.setPrevious(this.tail as DoublyNode<T>);
            this.tail = newNode;
        }
    }

    public getValues(reverse?: 'reverse'): void {
        if (!reverse) {
            super.getValues()
        } else {
            
        }

    }
}

const doublyLL = new DoublyLinkedList();
doublyLL.add(1)
doublyLL.add(2)
doublyLL.add(3)
doublyLL.add(4)
doublyLL.getValues()