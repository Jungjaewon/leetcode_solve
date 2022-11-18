class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        temp = rooms[0]
        while len(temp):
            temp_l = set()
            for n in temp:
                visited[n] = True
                for k in rooms[n]:
                    if not visited[k]:
                        temp_l.add(k)
            temp = list(temp_l)
        return all(visited)