# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        
        # Helper function for Preorder Traversal
        def dfs(node):
            if not node:
                # TODO: What should we append to `res` if the node is empty?
                res.append("N")
                return 
            
            # 1. Process the Root (append its value as a string to `res`)
            # 2. Recursively call DFS on the left child
            # 3. Recursively call DFS on the right child
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        # Start the traversal
        dfs(root)
        
        # Join the array into a single string separated by commas
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # Split the string back into a list of values
        vals = data.split(",")
        
        # A pointer to track which item in the array we are currently looking at!
        self.i = 0
        
        # Helper function to rebuild the tree
        def dfs():
            # Grab the current value from the array, and move the pointer forward!
            val = vals[self.i]
            self.i += 1
            
            # TODO: If `val` is our special "None" character... return None!
            if val == "N":
                return None
            
            
            # 1. Create a new TreeNode using the value (don't forget to convert it to an int!)
            # 2. Recursively build its left child: node.left = dfs()
            # 3. Recursively build its right child: node.right = dfs()
            
            # 4. Return the node!

            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
            
            
        return dfs()
