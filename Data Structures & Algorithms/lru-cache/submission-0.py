# 1. Define our Doubly Linked List Node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key -> Node

        # Create our Dummy boundary nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        # Connect them: Left <-> Right
        self.left.next = self.right
        self.right.prev = self.left

    # --- HELPER FUNCTIONS ---
    def remove(self, node: Node):
        # Connect node.prev to node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert(self, node: Node):
        # It should go right BEFORE self.right
        pre_node= self.right.prev


        node.next=self.right
        node.prev=pre_node

        pre_node.next=node
        self.right.prev=node


        

    # --- MAIN FUNCTIONS ---
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

        else:
            return -1    

    def put(self, key: int, value: int) -> None:
       
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)


        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]



        

