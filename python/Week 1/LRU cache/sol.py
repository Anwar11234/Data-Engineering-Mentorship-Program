class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # least recently used = head.next, most recently used = tail.prev
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.delete(lru)
            del self.cache[lru.key]
            
    def delete(self, node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insert(self, node):
        nxt = self.tail
        prv = self.tail.prev
        nxt.prev = node
        prv.next = node
        node.next = nxt
        node.prev = prv


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)