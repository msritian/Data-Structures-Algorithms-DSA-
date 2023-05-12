# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         from itertools import permutations 
#         return permutations(nums)
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        freq=[0]*len(nums)
        ds=[]

        def solve(nums,ds,ans,freq):
            if len(ds)==len(nums):
                ans.append(ds.copy())
                return
            for i in range(len(nums)):
                if freq[i]==0:
                    freq[i]=1
                    ds.append(nums[i])
                    solve(nums,ds,ans,freq)
                    freq[i]=0
                    ds.pop(-1)
        solve(nums,ds,ans,freq)
        return ans