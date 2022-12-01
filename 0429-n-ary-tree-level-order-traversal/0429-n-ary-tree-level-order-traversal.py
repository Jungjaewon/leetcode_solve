"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import defaultdict
        ans, ans_dict = list(), defaultdict(list)
        
        def dfs(level:int, root: 'Node'):
            if root is None:
                return 
            else:
                ans_dict[level].append(root.val)
                for node in root.children:
                    dfs(level + 1, node)
        dfs(0, root)
        for level in sorted(list(ans_dict.keys())):
            ans.append(ans_dict[level])
        return ans
        """
        from queue import Queue
        Q, ans = Queue(), list()
        
        if root:
            Q.put(root)
            
        while Q.qsize():
            qsize, temp_l = Q.qsize(), list()
            for _ in range(qsize):
                node = Q.get()
                temp_l.append(node.val)
                for n_c in node.children:
                    Q.put(n_c)
            ans.append(temp_l)    
        return ans
        """
        