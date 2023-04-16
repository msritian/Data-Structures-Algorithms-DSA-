# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        size=len(nums)
        if not size:
            return None
        mid=size//2
        return TreeNode(nums[mid],
        self.sortedArrayToBST(nums[:mid]),
        self.sortedArrayToBST(nums[mid+1:]))  