# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        def func(node: Optional[TreeNode]):
            if node is None:
                return []
            else:
                return [node.val] + func(node.left) + func(node.right)
        val_list = func(root)
        val_cnt_dict = Counter(val_list)
        max_cnt = max(val_cnt_dict.values())
        return [ x for x in val_cnt_dict if val_cnt_dict[x] == max_cnt]
        """
        cnt_dict = defaultdict(int)
        def func(node: Optional[TreeNode]):
            if node is None:
                return
            else:
                cnt_dict[node.val] += 1
                func(node.left)
                func(node.right)
        func(root)
        max_cnt = max(cnt_dict.values())
        return [ x for x in cnt_dict if cnt_dict[x] == max_cnt]