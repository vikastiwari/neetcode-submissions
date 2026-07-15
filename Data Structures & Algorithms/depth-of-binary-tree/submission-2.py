# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        answer=0

        while queue:

            length = len(queue)

            for i in range(length):
                top = queue.popleft()

                if top.left:
                    queue.append(top.left)

                if top.right:
                    queue.append(top.right)  

            answer+=1

        return answer        





        
        