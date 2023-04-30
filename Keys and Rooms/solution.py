class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[]
        visited=[False]*len(rooms)
        stack.append(0)
        results=[]
        while len(stack)>0:
            current=stack.pop()
            if not visited[current]:
                visited[current]=True
                results.append(current)
                for v in rooms[current]:
                    stack.append(v)
        return all(visited)
