class Solution:
    def minCut(self, s: str) -> int:
        t=[[-1 for j in range(2001)] for i in range(2001)]
        i=0
        j=len(s)
        
        def solve(s,i,j):
            if i>=j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            if s[i:j+1]==s[i:j+1][::-1]:
                t[i][j]=0
                return 0
            
            mn=float('inf')
            for k in range(i,j):
                if t[i][k]!=-1:
                    left=t[i][k]
                else:
                    left=solve(s,i,k)
                    t[i][k]=left
                if t[k+1][j]!=-1:
                    right=t[k+1][j]
                else:
                    right=solve(s,k+1,j)
                    t[k+1][j]=right
                temp=1+left+right
                if temp<mn:
                    mn=temp
            t[i][j]=mn
            return t[i][j]
        return solve(s,i,j)
                