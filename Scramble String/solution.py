class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mp={}
        def solve(s1,s2):
            
            if len(s1)!=len(s2):
                return False
            if len(s1)==0 and len(s2)==0:
                return True
            if len(s1)<=1:
                return False
            if s1==s2: 
                return True
            temp=s1
            temp+=" "
            temp+=s2
            if temp in mp:
                if mp[temp]==True:
                    return mp[temp]
            flag=False
            for i in range(1,len(s1)):
                if (solve(s1[:i+1],s2[:i+1]) == True and solve(s1[i:],s2[i:]) == True) or (solve(s1[:i+1],s2[i:])==True and solve(s1[i:],s2[:i+1]) == True):
                    flag=True
                    break
            mp[temp]=flag
            return flag
        return solve(s1,s2)