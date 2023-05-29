class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def solve(ip,op):
            if len(ip)==0:
                res.append(op[:])
                return
            for i in range(len(ip)):
                temp=ip[:i+1]
                if temp==temp[::-1]:
                    op1=op
                    op1.append(temp)
                    solve(ip[i+1:],op1)
                    op1.pop()
        solve(s,[])
        return res