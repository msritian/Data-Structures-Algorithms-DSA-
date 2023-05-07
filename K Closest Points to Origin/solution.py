class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap=[]
        heapq.heapify(self.heap)

        for point in points:
            heapq.heappush(self.heap,[-1*(point[0]**2+point[1]**2),point])
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        res=[]
        for v in self.heap:
            res.append(v[1])
        return res