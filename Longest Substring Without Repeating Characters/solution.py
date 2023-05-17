# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         i =0
#         j = 0
#         d={}
#         ans = 0
#         while j < len(s):
#             if s[j] not in d or i>d[s[j]]:
#                 ans = max(ans,(j-i+1))
#                 d[s[j]] = j
#             else:
#                 i = d[s[j]]+1
#                 ans = max(ans,(j-i+1))
#                 j-=1
#             j+=1
#         return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        i,j,mx=0,0,0
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1

            if len(mp)<j-i+1:
                while len(mp)<j-i+1:
                    mp[s[i]]-=1
                    if mp[s[i]]==0:
                        mp.pop(s[i])
                    i+=1
                j+=1
            elif len(mp)==j-i+1:
                mx=max(mx,j-i+1)
                j+=1
        return mx

        