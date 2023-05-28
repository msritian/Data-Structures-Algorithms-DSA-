class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Using DP
        m=len(s)
        s2=s[::-1]
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
                    arr[i][j]=0
        stx,sty,maxi=0,0,0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if arr[i][j]>maxi:
                    maxi=arr[i][j]
                    stx=i
                    sty=j

        res=""
        i=stx
        j=sty
        while i>0 and j>0:
            if arr[i][j]>0:
                res+=s[i-1]
                i-=1
                j-=1
            else:
                break
        return res