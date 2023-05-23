class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        #Matrix chain multiplication
        t=[[-1 for i in range(n+1)] for j in range(k+1)]
        
        def solve(k,n):
            if n==0 or n==1:
                return n
            if k==1:
                return n
            if t[k][n]!=-1:
                return t[k][n]
            mn=float('inf')
            l=1
            h=n
            while l<=h:
                mid=(l+h)//2
                if t[k-1][mid-1]!=-1:
                    left=t[k-1][mid-1]
                else:
                    left=solve(k-1,mid-1)
                    t[k-1][mid-1]=left
                
                if t[k][n-mid]!=-1:
                    right=t[k][n-mid]
                else:
                    right=solve(k,n-mid)
                    t[k][n-mid]=right
                temp=1+max(left,right)
                if left<right:
                    l=mid+1
                else:
                    h=mid-1
                mn=min(temp,mn)
            t[k][n]=mn
            return mn

        return solve(k,n)