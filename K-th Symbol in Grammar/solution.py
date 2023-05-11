class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(n,k):
            if n==1 and k==1:
                return 0
            mid=(2**(n-1))/2
            if k<= mid:
                return solve(n-1,k)
            else:
                return 1 if solve(n - 1, k - mid) == 0 else 0
        return solve(n,k)