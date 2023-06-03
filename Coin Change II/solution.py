class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        target=amount
        nums=coins
        t=[["" for j in range(target+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(target+1):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=1
        for i in range(1,len(nums)+1):
            for j in range(target+1):
                if nums[i-1]<=j:
                    t[i][j]=t[i][j-nums[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[len(nums)][target]