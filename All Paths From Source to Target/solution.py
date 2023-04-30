class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target=len(graph)-1
        lis=[]
        def ways(u,path):
            for v in graph[u]:
                if v==target:
                    lis.append(path+[v])
                ways(v,path+[v])        
        ways(0,[0])
        return lis