class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def condition(m,type):
            if nums[m]==target:
                if type==1:
                    if m>0 and nums[m-1]==target:
                        return 'left'
                    else:
                        return 'found'
                else:
                    if m<len(nums)-1 and nums[m+1]==target:
                        return 'right'
                    else:
                        return 'found'
            elif nums[m]<target:
                return 'right'
            else:
                return 'left'
        def search(l,h,type) -> int:
            while(l<=h):
                m=(l+h)//2
                # print(m)
                result=condition(m,type)
                # print(result)
                if result=='found':
                    return m
                elif result=='right':
                    l=m+1
                else:
                    h=m-1
            return -1
        def first_position(nums,target):
            return search(0,len(nums)-1,1)
        def last_position(nums,target):
            return search(0,len(nums)-1,2)
        
        return [first_position(nums,target),last_position(nums,target)]