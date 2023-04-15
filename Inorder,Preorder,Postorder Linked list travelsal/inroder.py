# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        self.trav(root,ls)
        return ls
    def trav(self,root,ls):
        if root == None:
            return
        else:
            self.trav(root.left,ls)
            ls.append(root.val)
            self.trav(root.right,ls)