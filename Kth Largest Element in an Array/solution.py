class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap=[]
        heapq.heapify(self.heap)
        
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        return self.heap[0]