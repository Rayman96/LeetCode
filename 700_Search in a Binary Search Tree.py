# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            
            elif root.val > val:
                if root.left:
                    return self.searchBST(root.left, val)
                else:
                    return None
            elif root.val < val:
                if root.right:
                    return self.searchBST(root.right, val)
                else:
                    return None
        else:
            return None