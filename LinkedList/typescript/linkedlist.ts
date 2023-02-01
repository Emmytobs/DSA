export class Node_<T=number> {
    private data: T
    private next: null | Node_<T>

    constructor(value: T) {
        this.data = value
        this.next = null
    }

    getData() {
        return this.data
    }
    getNext() {
        return this.next
    }

    setData(value: T){
        this.data = value
    }
    setNext(nextNode: Node_<T>) {
        this.next = nextNode
    }
    hasNext() {
        if (this.next instanceof Node_<T>) {
            return true
        } else {
            return false
        }
    }
}


export class LinkedList<T=number> {
    protected head: null | Node_<T>;
    protected tail: null | Node_<T>;

    constructor() {
        this.head = this.tail = null;
    }

    public isEmpty(): boolean {
        return this.head == null
    }

    public add(nodeValue: T): void {
        const newNode: Node_<T> = new Node_<T>(nodeValue);
        if (this.isEmpty()) {
            this.head = this.tail = newNode;
        }
        else {
            // Since the Node in the tail is the ccurrent last node, by using the setNext method, we establish a link from the tail to the new node.
            this.tail!.setNext(newNode);
            this.tail = newNode;
        }
    }

    public getValues(): void {
        if (this.isEmpty()) {
            console.error("No data");
        }
        else {
            let cursor: Node_<T> = this.head as Node_<T>;
            while (cursor instanceof Node_<T>) {
                console.log(cursor.getData())
                cursor = cursor.getNext() as Node_<T>;
            }
        }
    }
}

// Test
// const linkedList = new LinkedList();
// linkedList.add(1);
// linkedList.add(2);
// linkedList.getValues()


