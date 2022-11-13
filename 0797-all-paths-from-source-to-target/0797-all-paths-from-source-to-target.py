class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, m = list(), len(graph)
        visited, history = [False] * m, [0]
        def dfs(node):
            if m - 1 == node:
                ans.append([*history])
                return
            else:
                for dest in graph[node]:
                    if not visited[dest]:
                        visited[dest] = True
                        history.append(dest)
                        dfs(dest)
                        visited[dest] = False
                        del history[-1]
        dfs(0)
        return ans