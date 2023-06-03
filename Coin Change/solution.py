class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        target=amount
        nums=coins
        t=[["" for j in range(target+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(target+1):
                if j==0:
                    t[i][j]=0
                if i==0:
                    t[i][j]=float('inf')-1

            for j in range(1,target+1):
                if j%nums[0]==0:
                    t[1][j]=j/nums[0]
                else:
                    t[1][j]=float('inf')-1
        for i in range(2,len(nums)+1):
            for j in range(1,target+1):
                if nums[i-1]<=j:
                    t[i][j]=min(1 + t[i][j-nums[i-1]],t[i-1][j])  
                else:
                    t[i][j]=t[i-1][j]
        if t[len(nums)][target]==float(inf)-1:
            return -1
        return int(t[len(nums)][target])