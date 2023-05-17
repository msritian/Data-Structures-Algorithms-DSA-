from collections import defaultdict
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # mp={i:0 for i in fruits}
        mp = defaultdict(int)
        i,j,mx=0,0,0
        k=2
        if len(fruits)<=2:
            return len(fruits)
        if len(Counter(fruits))<2:
            return len(fruits)
        while j<len(fruits):
            mp[fruits[j]]+=1

            if len(mp)<k:
                j+=1
            elif len(mp)==k:
                mx=max(mx,j-i+1)
                j+=1
            elif len(mp)>k:
                print(mp)
                while len(mp)>k:
                    mp[fruits[i]]-=1
                    if mp[fruits[i]]==0:
                        del mp[fruits[i]]
                    i+=1
                j+=1
        return mx
