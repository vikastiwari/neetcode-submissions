"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old_to_new = {}

        # dfs will return the CLONED version of whatever node we pass into it!
        def dfs(curr_node):
            
            # Base Case: We already cloned this node before! Stop the infinite loop!
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            # 1. Create the clone
            copy_node = Node(curr_node.val)
            
            # 2. Add it to our Hash Map immediately!
            old_to_new[curr_node] = copy_node
            
            # 3. Clone all the neighbors!
            for nei in curr_node.neighbors:
                # Recursively call dfs to get the cloned neighbor, and append it
                # TODO: Append the result of dfs(nei) to copy_node.neighbors!
                copy_node.neighbors.append(dfs(nei))
                
            return copy_node

        return dfs(node)
