# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        answer=[]

        while queue:
            length=len(queue)

            for i in range(length):
                top=queue.popleft()
                if(i==0):
                    answer.append(top.val)

                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return answer            


        