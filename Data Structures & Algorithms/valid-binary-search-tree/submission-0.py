# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"),float("inf"))

    def dfs(self, root: Optional[TreeNode],min:float,max:float) -> bool:

        if not root:
            return True

        if not (min<root.val<max):
            return False    

        left = self.dfs(root.left,min,root.val)
        right =self.dfs(root.right,root.val,max)    

        return left and right
    

