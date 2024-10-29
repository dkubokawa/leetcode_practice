class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least_recent = Node(0, 0)
        self.most_recent = Node(0, 0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent

    def insert(self, node: Node):
        # Need to insert to the left of the most_recent dummy Node and fix the ptrs
        prev = self.most_recent.prev
        next = self.most_recent
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def remove(self, node: Node):
        #  prev -> 0 1 2 <- next, node is 1, looking to remove
        #  prev.next to pt to next, next.prev to pt to prev
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.least_recent.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)