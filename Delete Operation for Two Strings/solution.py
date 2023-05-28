class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s=word1
        m=len(s)
        s2=word2
        n=len(s2)
        arr=[["" for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    arr[i][j]=0
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==s2[j-1]:
                    arr[i][j]= 1+arr[i-1][j-1]
                else:
                    arr[i][j]=max(arr[i-1][j],arr[i][j-1])
        return len(word1) - arr[m][n] + len(word2) - arr[m][n]