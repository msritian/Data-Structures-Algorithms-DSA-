from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp={}
        mini=float('inf')
        ans=""
        for i in t:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        count=len(mp)
        i,j=0,0
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]-=1
                if mp[s[j]]==0:
                    count-=1
            while count==0:
                if mini>j-i+1:
                    mini=min(mini,j-i+1)
                    ans=s[i:i+mini]
                if s[i] in mp:
                    mp[s[i]]+=1
                    if mp[s[i]]==1:
                        count+=1
                    i+=1
                else:
                    i+=1
            j+=1
        return ans
                     
            