class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        add,i,j=0,0,0
        k=target
        mx=float('inf')
        while j<len(nums):
            add+=nums[j]

            if add<k:
                j+=1
            if add>=k:
                while add>=k:
                    mx=min(mx,(j-i+1))
                    add-=nums[i]
                    i+=1
                j+=1
        return mx if mx!=float('inf') else 0
