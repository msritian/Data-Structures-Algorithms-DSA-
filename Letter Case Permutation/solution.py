class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        inp=s
        op=[]
        ans=[]
        def solve(inp,op):
            if inp=="":
                ans.append("".join(op))
                return
            if inp[0].isalpha():
                op1=op[:]
                op2=op[:]
                op1+=inp[0].lower()
                op2+=inp[0].upper()
                inp=inp[1:]
                solve(inp,op1)
                solve(inp,op2)
                return
            else:
                op1=op
                op1+=inp[0]
                inp=inp[1:]
                solve(inp,op1)
                return
        solve(inp,op)
        return ans