# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         low=0
#         high=len(nums)-1
#         while (low<high):
#             mid=(high+low)//2
#             if mid>low and mid<high:
#                 if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
#                     return mid
#                 elif nums[mid-1]>nums[mid]:
#                     high=mid-1
#                 else:
#                     low=mid+1
#             elif mid==0:
#                 if nums[0]>nums[1]:
#                     return 0
#                 else:
#                     return 1      
#             elif mid==high:
#                 if nums[mid]>nums[mid-1]:
#                     return high
#                 else:
#                     return high-1
        

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 1:
            return 0
        
        while left < right:
            mid = (left + right)//2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
                
            else:
                right = mid - 1
        
        return  right if nums[right] > nums[mid] else mid
            