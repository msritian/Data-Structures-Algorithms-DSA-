class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        inp=nums
        op=[]
        ans=[]
        def solve(inp,op):
            if inp==[]:
                if op not in ans:
                    ans.append(op)
                    return
            if inp!=[]:
                op1=op[:]
                op2=op[:]
                op2.append(inp[0]) 
                inp=inp[1:]
                solve(inp,op1)
                solve(inp,op2)
                return
        inp.sort()
        solve(inp,op)
        return ans