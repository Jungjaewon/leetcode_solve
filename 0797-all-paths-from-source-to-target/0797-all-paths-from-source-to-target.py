class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, m = list(), len(graph)
        visited, history = [False] * m, [0]
        def dfs(node):
            if m - 1 == node:
                ans.append(history[:])
                return
            else:
                for dest in graph[node]:
                    if not visited[dest]:
                        #visited[dest] = True
                        history.append(dest)
                        dfs(dest)
                        #visited[dest] = False
                        del history[-1]
        dfs(0)
        return ans
    #def allPathsSourceTarget(self, g, cur=0):
    #    if cur == len(g) - 1: return [[len(g) - 1]]
    #    return [([cur] + path) for i in g[cur] for path in self.allPathsSourceTarget(g, i)]
    #def allPathsSourceTarget(self, graph):
    #    def dfs(cur, path):
    #        if cur == len(graph) - 1: res.append(path)
    #        else:
    #            for i in graph[cur]: dfs(i, path + [i])
    #    res = []
    #    dfs(0, [0])
    #    return res
    # https://leetcode.com/problems/all-paths-from-source-to-target/discuss/118691/C%2B%2BPython-Backtracking