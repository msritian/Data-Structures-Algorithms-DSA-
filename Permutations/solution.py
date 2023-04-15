class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations 
        return permutations(nums)
        