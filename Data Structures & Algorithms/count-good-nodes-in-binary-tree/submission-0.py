# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer=0

        if not root:
            return answer

        max=0
        queue = collections.deque([(root,root.val)])

        while  queue:
            length=len(queue)

            for i in range(length):
                top,curr_max = queue.popleft()
                if top.val>=curr_max:
                    answer+=1
                    curr_max=top.val


                if top.left:
                    queue.append((top.left,curr_max))

                if top.right:
                    queue.append((top.right,curr_max))          


        return answer
        