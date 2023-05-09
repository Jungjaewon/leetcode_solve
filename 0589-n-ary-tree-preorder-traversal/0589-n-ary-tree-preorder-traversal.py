"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        else:
            sub_list = list()
            sub_list.append(root.val)
            for ch in root.children:
                res = self.preorder(ch)
                if len(res):
                    if isinstance(res, list):
                        sub_list.extend(res)
                    else:
                        sub_list.append(res)
            return sub_list