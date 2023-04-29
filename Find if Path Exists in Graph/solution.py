class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.data=[[] for _ in range(n)]
        for v1,v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
        visited=[False]*len(self.data)
        visited[source]=True
        queue=[source]
        while queue:
            ele=queue.pop(0)
            if ele==destination:
                return True
            for v in self.data[ele]:
                if not visited[v]:
                    visited[v]=True
                    queue.append(v)
        return False