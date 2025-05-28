class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class Doubly:
    def __init__(self, cap, cach):
        self.cap = cap
        self.cach = cach

    def insert(self, head, val, k, tail):
        new_node = Node(val, k)
        self.cach[k] = new_node
        if head is None:
            head = tail = new_node
        else:
            new_node.next = head
            head.prev = new_node
            head = new_node
        return head, tail

    def rem(self, head, key, value, tail):
        # Add new node at head
        new_node = Node(value, key)
        self.cach[key] = new_node
        new_node.next = head
        if head:
            head.prev = new_node
        head = new_node

        # Remove the old tail node (LRU)
        if tail:
            del self.cach[tail.key]
            if tail.prev:
                tail = tail.prev
                tail.next = None
            else:
                # Only one node existed
                head = None
                tail = None
        return head, tail

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.ddl = Doubly(self.cap, self.cache)
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        found_node = self.cache[key]
        if found_node == self.head:
            return found_node.val

        # Unlink found_node
        if found_node.prev:
            found_node.prev.next = found_node.next
        if found_node.next:
            found_node.next.prev = found_node.prev
        if found_node == self.tail:
            self.tail = found_node.prev

        # Move to front
        found_node.prev = None
        found_node.next = self.head
        if self.head:
            self.head.prev = found_node
        self.head = found_node

        return found_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to front
            self.cache[key].val = value
            self.get(key)
            return

        if self.cap == 0:
            self.head, self.tail = self.ddl.rem(self.head, key, value, self.tail)
        else:
            self.head, self.tail = self.ddl.insert(self.head, value, key, self.tail)
            self.cap -= 1
