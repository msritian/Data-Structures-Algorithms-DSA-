class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        ans=[]
        def solve(index,candidates,target,ds,ans):
            if index>=len(candidates):
                return
            if index==len(candidates)-1:
                if target==0:
                    ans.append(ds.copy())
                    return
            #pick an element
            if candidates[index]<=target:
                ds.append(candidates[index])
                solve(index,candidates,target-candidates[index],ds,ans)
                ds.pop(-1)

            #not pick
            solve(index+1,candidates,target,ds,ans)
        solve(0,candidates,target,ds,ans)
        return ans