"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        if root is None:
            return []
        else:
            sub_list = list()
            for ch in root.children:
                sub_list += self.postorder(ch)
            sub_list.append(root.val)
            return sub_list
        """
        """
        if root is None:
            return []
        else:
            sub_list = list()
            for ch in root.children:
                res = self.postorder(ch)
                if len(res):
                    if isinstance(res, list):
                        for r in res:
                            sub_list.append(r)
                    else:
                        sub_list.append(res)
            sub_list.append(root.val)
            return sub_list
        """
        if root is None:
            return []
        else:
            sub_list = list()
            for ch in root.children:
                res = self.postorder(ch)
                if len(res):
                    if isinstance(res, list):
                        sub_list.extend(res)
                    else:
                        sub_list.append(res)
            sub_list.append(root.val)
            return sub_list