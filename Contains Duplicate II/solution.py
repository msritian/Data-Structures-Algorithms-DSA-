class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i,j=0,0
        mp={}
        if k<len(nums):
            k+=1
        else:
            k=len(nums)
        while j<len(nums):
            if nums[j] in mp:
                mp[nums[j]]+=1
            else:
                mp[nums[j]]=1
            if j-i+1 < k:
                j+=1
            elif j-i+1 == k:
                if len(mp)<k:
                    return True
                mp[nums[i]]-=1
                if mp[nums[i]]==0:
                    mp.pop(nums[i])
                i+=1
                j+=1
        return False
