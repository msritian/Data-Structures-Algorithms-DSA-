class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index=0
        lis = [i for i in range(1, n + 1)]
        k=k-1
        
        def solve(lis,index,k):
            if len(lis)==1:
                return lis[-1]
            index=(index+k) % len(lis)
            lis.pop(index)
            return solve(lis,index,k)
        return solve(lis,index,k)