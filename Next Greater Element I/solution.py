class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res={}
        for i in range(len(nums2)-1,-1,-1):
            if len(stack)==0:
                res[nums2[i]]=-1
            elif len(stack)!=0 and stack[-1]>nums2[i]:
                res[nums2[i]]=stack[-1]
            elif len(stack)!=0 and stack[-1]<=nums2[i]:
                while(len(stack)!=0 and stack[-1]<=nums2[i]):
                    stack.pop()
                if len(stack)==0:
                    res[nums2[i]]=-1
                else:
                    res[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        l=[]
        for i in nums1:
            l.append(res[i])
        return l