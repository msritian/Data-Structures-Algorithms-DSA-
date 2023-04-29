class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num_nodes=max(map(max, edges))
        self.data=[[] for _ in range(num_nodes+1)]
        for v1,v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
        for i,neighbors in enumerate(self.data):
            if len(neighbors)==len(edges):
                return i