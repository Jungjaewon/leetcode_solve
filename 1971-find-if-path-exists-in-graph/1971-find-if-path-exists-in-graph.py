class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        #if source == destination:
        #    return True
        
        adj_dict = defaultdict(list)
        for edge in edges:
            s,e = edge
            adj_dict[s].append(e)
            adj_dict[e].append(s)
        
        for edge in adj_dict:
            adj_dict[edge] = list(set(adj_dict[edge]))
        
        if destination in adj_dict[source]:
            return True
        else:
            visited = [False] * n
            visited[source] = True
            temp_list = adj_dict[source]
            def func(temp_list):
                for n in temp_list:
                    if not visited[n]:
                        visited[n] = True
                        func(adj_dict[n])
            func(temp_list)
            return visited[destination]