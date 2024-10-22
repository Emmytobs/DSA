class _Node {
    prev: _Node | null = null;
    next: _Node | null = null;
    key: number = 0;
    value: number = 0;
    constructor(key: number, value: number) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    capacity = 0;
    noOfItems = 0
    left = new _Node(0, 0)
    right = new _Node(0, 0)
    cache: Record<number, _Node> = {}
    constructor(capacity: number) {
        this.capacity = capacity
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    get(key: number): number {
        if (key in this.cache) {
            const node = this.cache[key];
            this.remove(node)
            this.add(node);
            return node.value;
        }
        return -1
    }

    put(key: number, value: number): void {
        let node = new _Node(key, value)
        const isAtCapacity = this.noOfItems === this.capacity;
        if (!!this.cache[key]) {
            const nodeWithExistingKey = this.cache[key] as _Node;
            this.remove(nodeWithExistingKey)
        }
        else if (isAtCapacity) {
            const lruNode = this.left.next as _Node;
            const lruKey = lruNode.key;
            delete this.cache[lruKey]
            this.remove(lruNode);
        }
        this.add(node)
        this.cache[key] = node
        if (!isAtCapacity) this.noOfItems += 1;
    }

    private remove(node: _Node) {
        const prevNode = node.prev
        const nextNode = node.next
        if (prevNode) prevNode.next = nextNode
        if (nextNode) nextNode.prev = prevNode
    }

    /**
    Adds before the tail of the LinkedList
    */
    private add(node: _Node) {
        const prevToRight = this.right.prev as _Node;
        prevToRight.next = node;
        this.right.prev = node;
        node.next = this.right;
        node.prev = prevToRight;
    }
}

const lruCache = new LRUCache(2)
lruCache.put(2,6)
lruCache.get(1)
lruCache.put(1, 5)
lruCache.put(1, 2)
// lruCache.get(1)
// lruCache.get(2)

let node = lruCache.left
while (node.next) {
    node = node.next;
    console.log(node.value)
}


/* Initial implementation - get() and put() don't run in O(1) time, so it's not efficient

type CacheValue = {
    data: number;
    age: number
}

class LRUCache {
    cacheDataCount = 0;
    maxAge = 0
    capacity = 0;
    lruKey = 0;
    cacheData: Record<number, CacheValue> = {}
    constructor(capacity: number) {
        this.capacity = capacity
    }

    get(key: number): number {
        if (key in this.cacheData) {
            const result = this.cacheData[key]
            const incrementedAge = result.age + 1
            this.maxAge += 1;
            this.cacheData[key] = { ...result, age: this.maxAge }
            return result.data
        }
        return -1;
    }

    put(key: number, value: number): void {
        this.maxAge += 1

        const keyExists = this.cacheData[key] != undefined;
        if (keyExists) {
            this.cacheData[key] = { data: value, age: this.maxAge }
            return;
        }

        const cacheIsFull = this.cacheDataCount == this.capacity;
        if (cacheIsFull) {
            // replace the lru key-value pair from the cache's data with the new key-value pair
            let lruKey = null;
            let minAge = Infinity;
            for (const key in this.cacheData) {
                const { age } = this.cacheData[key]
                if (age < minAge) {
                    minAge = age;
                    lruKey = key
                }
            }
            delete this.cacheData[lruKey]
            this.cacheData[key] = { data: value, age: this.maxAge };
            console.log("lruKey", lruKey, this.cacheData)
            return;
        }
    
        this.cacheData[key] = { data: value, age: this.maxAge };
        console.log(this.cacheData)
        this.cacheDataCount += 1
    }
}
*/
/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */