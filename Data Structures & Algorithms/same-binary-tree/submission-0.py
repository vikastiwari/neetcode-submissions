# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer=True

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            top1=queue1.popleft()
            top2=queue2.popleft()

            if top1 is None and top2 is None:
                continue
            elif top1 is None and top2 is not None:
                return False
            elif top1 is not None and top2 is None:
                return False 

            if top1.val != top2.val:
                return False
            else:
                queue1.append(top1.left)
                queue1.append(top1.right)
                queue2.append(top2.left)
                queue2.append(top2.right)


                if len(queue1)!=len(queue2):
                    return False               

        if (queue1 is None and queue2 is not None) or (queue2 is None and queue1 is not None):
            return False     

        return answer
        