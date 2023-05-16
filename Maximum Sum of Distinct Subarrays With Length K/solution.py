class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int: 
        i,j,add,mx,count=0,0,0,0,0
        mp={i:0 for i in nums}

        while j<len(nums):
            mp[nums[j]]+=1
            if mp[nums[j]]==1:
                count+=1
            add+=nums[j]
            if (j-i+1)<k:
                j+=1
            elif (j-i+1)==k:
                if count==k:
                    mx=max(add,mx)
                mp[nums[i]]-=1
                if mp[nums[i]]==0:
                    count-=1
                add-=nums[i]
                i+=1
                j+=1
        return mx