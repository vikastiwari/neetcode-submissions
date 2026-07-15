"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        # This dictionary maps: Original Node -> Cloned Node
        old_to_copy = {}
        
        # --- PASS 1: Build the Clones ---
        curr = head
        while curr:
            # 1. Create a brand new node with just the value (no pointers yet)
            # 2. Put it in the dictionary
            
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next
            
            
        # --- PASS 2: Wire the Pointers ---
        curr = head
        while curr:
            # Grab the cloned node we just made from the dictionary
            copy_node = old_to_copy[curr]
            
            # 1. Wire the 'next' pointer
            # If the original node has a 'next', look up its clone in the dictionary and attach it!
            if curr.next:
                copy_node.next = old_to_copy[curr.next]
                
            # 2. Wire the 'random' pointer
            # If the original node has a 'random', look up its clone in the dictionary and attach it!
            if curr.random:
                copy_node.random = old_to_copy[curr.random]
                
            curr = curr.next
            
        # Finally, return the clone of the head!
        return old_to_copy[head]
      