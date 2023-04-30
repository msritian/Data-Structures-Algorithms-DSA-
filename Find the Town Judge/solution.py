class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        self.data=[[] for _ in range(n+1)]
        d={}
        for v1,v2 in trust:
            self.data[v1].append(v2)
            # self.data[v2].append(v1)
        for i,neighbors in enumerate(self.data):
            d[i]=neighbors
        print(d)
        value = list({i for i in d if d[i]==[]})
        d2={}
        for v in value:
            count=0
            for val in d.values():
                if v in val:
                    count+=1
            d2[v]=count
        judge=max(d2)
        if d2.get(judge)==n-1:
            return judge
        else:
            return -1