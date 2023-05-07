class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        self.heap=[]
        heapq.heapify(self.heap)

        for point in arr:
            heapq.heappush(self.heap,[-1*abs(point-x),-1*point])
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        res=[]
        for v in self.heap[::-1]:
            res.append(-v[1])
        return sorted(res)