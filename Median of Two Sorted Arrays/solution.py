class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import math
        nums1.extend(nums2)
        nums1=sorted(nums1)
        if len(nums1)%2==0:
            return float(((nums1[int(len(nums1)/2)-1])+(nums1[int(len(nums1)/2)]))/2)
        else:
            return nums1[math.floor(len(nums1)/2)]
        