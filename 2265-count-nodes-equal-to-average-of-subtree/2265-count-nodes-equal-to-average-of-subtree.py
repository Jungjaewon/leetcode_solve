# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = [0]
        def func(node:TreeNode):
            if node is None:
                return []
            else:
                v,n,v_list = node.val,1,[]
                if node.left is not None:
                    return_v = func(node.left)
                    if return_v:
                        v_list.extend(return_v)
                if node.right is not None:
                    return_v = func(node.right)
                    if return_v:
                        v_list.extend(return_v)
                v += sum(v_list)
                n += len(v_list)
                avg = int(v / float(n))
                #print(f'v : {node.val}, v_list : {v_list}, n : {n}, {avg == node.val}, avg : {avg}')
                if avg == node.val:
                    ans[0] += 1
                return [node.val] + v_list
        func(root)
        return ans[0]