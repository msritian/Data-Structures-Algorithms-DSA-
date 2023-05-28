class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Using DP
        a=nums
        n = len(a)
 
        # Creating the sorted list
        b = sorted(list(set(a)))
        m = len(b)
    
        # Creating dp table for storing
        # the answers of sub problems
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    
        # Finding Longest common Subsequence of the two arrays
        for i in range(n+1):
    
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif a[i-1] == b[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]