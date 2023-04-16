# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def val(root,low,high):
            if root is None:
                return True
            if not (low < root.val < high):
                return False
            return val(root.right,root.val,high) and val(root.left,low,root.val)
        return val(root,-inf,inf)