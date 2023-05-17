class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp={i:0 for i in fruits}
        i,j,mx=0,0,0
        k=2
        while j<len(fruits):
            mp[fruits[j]]+=1

            if len(mp)<k:
                j+=1
            elif len(mp)==k:
                mx=max(mx,j-i+1)
                j+=1
            elif len(mp)>k:
                while len(mp)>k:
                    mp[fruits[i]]-=1
                    if mp[fruits[i]]==0:
                        mp.pop(fruits[i])
                    i+=1
                j+=1
        return mx
