# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ans = []
        
        def same(self, node1, node2):
            if node1.val == node2.val:
                if node1.left:
                    if node2.left:
                        same(self,node1.left, node2.left)
                    else:
                        ans.append(1)
                if node2.left:
                    if node1.left:
                        same(self,node1.left, node2.left)
                    else:
                        ans.append(1)
                if node1.right:
                    if node2.right:
                        same(self,node1.right, node2.right)
                    else:
                        ans.append(1)
                if node2.right:
                    if node1.right:
                        same(self,node1.right, node2.right)
                    else:
                        ans.append(1)
                ans.append(0)
            else:
                ans.append(1)
            
        if p and q:
            same(self, p, q)
            if 1 in ans:
                return False
            else:
                return True
        elif not p and not q:
            return True
            
        else:
            return False