class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp={}
        for i in p:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        count=len(mp)
        i,j=0,0
        k=len(p)
        ans=[]
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]-=1
                if mp[s[j]]==0:
                    count-=1
            
            if (j-i+1)<k:
                j+=1
            
            elif (j-i+1)==k:
                if count==0:
                    ans.append(i)
                if s[i] in mp:
                    mp[s[i]]+=1
                    if mp[s[i]]==1:
                        count+=1
                i+=1
                j+=1
        return ans

