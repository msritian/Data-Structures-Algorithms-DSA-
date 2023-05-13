class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        inp=nums
        op=[]
        ans=[]
        def solve(inp,op):
            if inp==[]:
                ans.append(op)
                return
            op1=op[:]
            op2=op[:]
            op2.append(inp[0])
            inp=inp[1:]
            solve(inp,op1)
            solve(inp,op2)
            return
        solve(inp,op)
        return ans