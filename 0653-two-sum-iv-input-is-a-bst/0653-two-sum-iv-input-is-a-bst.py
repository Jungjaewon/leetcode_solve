# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def func(node: Optional[TreeNode]):
            if node is None:
                return []
            else:
                return [node.val] + func(node.left) + func(node.right)
        numbers = dict(Counter(func(root)))
        
        if len(numbers) in [0,1]:
            return False
        
        for n in numbers:
            gap = k - n
            if gap == n:
                if gap in numbers and numbers[gap] > 1:
                    return True
            else:
                 if gap in numbers:
                    return True
        return False