# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Base case!
        if not preorder or not inorder:
            return None
            
        # 2. Build the root, find it in the inorder array
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # 3. Slice BOTH arrays correctly!
        # Left gets the next 'mid' items from preorder, and everything left of mid from inorder.
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0 : mid])
        
        # Right gets the rest of the preorder items, and everything right of mid from inorder.
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])
        
        return root
