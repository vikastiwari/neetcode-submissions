# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _,maxPath = self.dfs(root)
        return maxPath

    def dfs(self, root: Optional[TreeNode]) -> (int,int):  

        if not root:
            return (0,float('-inf')) 

        left_branch, left_pathsum = self.dfs(root.left)
        right_branch, right_pathsum = self.dfs(root.right)  

        left_branch = max(0, left_branch)
        right_branch = max(0, right_branch)

        max_branch_sum = root.val + max(left_branch,right_branch)
        my_path = left_branch+right_branch+root.val
        max_pathsum = max(my_path,left_pathsum,right_pathsum)




        return (max_branch_sum,max_pathsum)
        
