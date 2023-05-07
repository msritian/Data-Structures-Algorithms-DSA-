class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        print(words)
        words=dict(Counter(words))
        self.heap=[]
        heapq.heapify(self.heap)

        for val,freq in words.items():
            heapq.heappush(self.heap,[-1*freq,val])
            # if len(self.heap)>k:
            #     heapq.heappop(self.heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(self.heap)[1])
        # for v in self.heap[::-1]:
        #     res.append(v[1])
        return res