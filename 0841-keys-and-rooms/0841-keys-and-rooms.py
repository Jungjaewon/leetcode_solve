class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        
        def helper(room_n):
            visited[room_n] = True
            for n in rooms[room_n]:
                if not visited[n]:
                    helper(n)
        helper(0)
        return all(visited)
        
        """
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
        """