class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Using DP
        m=len(s)
        n=len(t)
        arr=[["" for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    arr[i][j]=0
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    arr[i][j]= 1+arr[i-1][j-1]
                else:
                    arr[i][j]=max(arr[i-1][j],arr[i][j-1])
        return arr[m][n]==len(s)