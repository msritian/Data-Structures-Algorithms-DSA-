class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(t,curr,ind):
            if(t==0):
                res.append(curr.copy())
                return
            for i in range(ind,len(candidates)):
                if(i>ind and candidates[i]==candidates[i-1]):
                    continue
                if(candidates[i]>t):
                    break
                curr.append(candidates[i])
                helper(t-candidates[i],curr,i+1)
                curr.pop() 
        candidates.sort()
        res,curr=[],[]
        helper(target,curr,0)
        return res