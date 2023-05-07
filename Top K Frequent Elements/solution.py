class Solution:
    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=dict(Counter(nums))
        self.heap=[]
        heapq.heapify(self.heap)

        for val,freq in nums.items():
            heapq.heappush(self.heap,[freq,val])
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        res=[]
        for v in self.heap:
            res.append(v[1])
        return res
    