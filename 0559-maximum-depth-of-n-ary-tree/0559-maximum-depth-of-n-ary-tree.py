"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:   
        if root is None:
            return 0
        else:
            ans = 0
            from queue import Queue
            q = Queue()
            q.put(root)
            while q.qsize():
                qsize = q.qsize()
                for _ in range(qsize):
                    node = q.get()
                    for ch in node.children:
                        if ch:
                            q.put(ch)
                ans += 1
            return ans
        
        
        