class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.dfs(root)
        return self.max_diameter
        
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
            
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        
        # We just update the global score right here! O(1) math!
        self.max_diameter = max(self.max_diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)
