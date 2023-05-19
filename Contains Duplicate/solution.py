from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp=dict(Counter(nums))
        if len(mp)<len(nums):
            return True
        else:
            return False