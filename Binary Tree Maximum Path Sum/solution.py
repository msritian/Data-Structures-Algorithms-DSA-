# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.res=-1000
        self.ans(root,self.res)
        return self.res
    
    def ans(self,root,res):
        if(root==None):
            return 0
        l=self.ans(root.left,self.res)
        r=self.ans(root.right,self.res)
        
        temp=max(max(l,r)+root.val,root.val)
        answer=max(temp,l+r+root.val)
        self.res=max(self.res,answer)
        return temp
