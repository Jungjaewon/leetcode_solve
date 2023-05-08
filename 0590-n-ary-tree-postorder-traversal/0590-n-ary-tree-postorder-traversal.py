"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        else:
            sub_list = list()
            for ch in root.children:
                sub_list += self.postorder(ch)
            sub_list.append(root.val)
            return sub_list