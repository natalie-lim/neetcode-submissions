class Node:
    def __init__(self, key, val, prev_node, next_node):
        self.key = key
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.d = {} # key, node
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        node = None
        if key in self.d:
            node = self.d[key]
        else:
            return -1

        if node is self.tail:
            return node.val

        prev = node.prev_node
        n = node.next_node
        if prev is not None:
            prev.next_node = n
        if n is not None:
            n.prev_node = prev
        if node == self.head:
            self.head = n if n else None
        node.prev_node = self.tail
        node.next_node = None
        self.tail.next_node = node
        self.tail = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            if node is not self.tail:
                prev = node.prev_node
                n = node.next_node
                if prev is not None:
                    prev.next_node = n
                if n is not None:
                    n.prev_node = prev
                if node == self.head:
                    self.head = n if n else None
                node.prev_node = self.tail
                node.next_node = None
                self.tail.next_node = node
                self.tail = node
            return

        self.curr_size += 1
        if self.curr_size > self.capacity:
            head_key = self.head.key
            next_head = self.head.next_node
            self.head.next_node = None
            if next_head is not None:
                next_head.prev_node = None
            if head_key in self.d:
                del self.d[head_key]
            self.head = next_head
            self.curr_size -= 1

        node = Node(key, value, self.tail, None)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next_node = node
        self.tail = node
        self.d[key] = node