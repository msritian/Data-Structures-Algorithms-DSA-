# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root: Optional[TreeNode], targetSum: int,sum: int) -> bool:
        if root==None:
            return False
        if root.left==None and root.right==None:
            sum+=root.val
            if sum==targetSum:
                return True
        return self.helper(root.left, targetSum, sum+root.val) or self.helper(root.right, targetSum, sum+root.val)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum=0
        return self.helper(root,targetSum,sum)