# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a_dict = defaultdict(list)
        def avg(data):
            return sum(data) / float(len(data))
        def func(root, level):
            if root is None:
                return
            else:
                a_dict[level].append(root.val)
                func(root.left, level + 1)
                func(root.right, level + 1)
        func(root, 0)
        return [avg(a_dict[key]) for key in sorted(a_dict.keys())]
                