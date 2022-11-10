# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_d, sum_v = [0], [0]
        def helper(depth,  root:Optional[TreeNode]):
            if root is None:
                return
            if depth > max_d[0]:
                sum_v[0], max_d[0] = 0, depth
            if depth == max_d[0]:
                sum_v[0] += root.val
            
            helper(depth + 1, root.left)
            helper(depth + 1, root.right)
        helper(0, root)
        return sum_v[0]
        """
        result_dict, result_list = defaultdict(list), list()
        def helper(result_list, depth, root:Optional[TreeNode]):
            if root is None:
                return
            else:
                result_list.append([depth, root.val])
                #if root.left:
                helper(result_list, depth + 1, root.left)
                #if root.right:
                helper(result_list, depth + 1, root.right)
        helper(result_list, 0, root)
        for depth, val in result_list:
            result_dict[depth].append(val)
        d_depth = sorted(result_dict.keys())[-1]
        return sum(result_dict[d_depth])
        """
            