# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]

        if not root:
            return []

        queue = collections.deque([root])

        while queue:
            length=len(queue)
            tmp = []

            for i in range(length):
                top=queue.popleft()
                tmp.append(top.val)

                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)    

            answer.append(tmp)   
        return answer     




        