class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        add=0
        for i in nums:
            add+=i
        if target>add:
            return 0
        if (add-target)%2==1:
            return 0
        target=int((add-target)/2)
        t=[["" for j in range(target+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(target+1):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=1
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j-nums[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[len(nums)][target]
                