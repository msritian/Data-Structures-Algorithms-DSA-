class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out=s.split(" ")
        out=list(filter(lambda x:x!='', out))
        return len(out[len(out)-1])