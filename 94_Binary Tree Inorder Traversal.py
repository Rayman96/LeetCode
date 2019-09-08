# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
                
        def next(self,root,ans):
            if root:
                if root.left:
                    next(self,root.left,ans)
                ans.append(root.val)
                if root.right:
                    next(self,root.right,ans)
            # return ans
                    
        if root:
            next(self,root,ans)
        return ans