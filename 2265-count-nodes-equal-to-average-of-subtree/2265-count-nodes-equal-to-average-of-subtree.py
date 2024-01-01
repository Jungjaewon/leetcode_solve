# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
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
        """
        """
        ans = [0]
        def func(node:TreeNode):
            if node is None:
                return []
            else:
                v_list = [node.val]
                if node.left is not None:
                    return_v = func(node.left)
                    if return_v:
                        v_list.extend(return_v)
                if node.right is not None:
                    return_v = func(node.right)
                    if return_v:
                        v_list.extend(return_v)
                avg = int( sum(v_list) / float(len(v_list)))
                #print(f'v : {node.val}, v_list : {v_list}, n : {n}, {avg == node.val}, avg : {avg}')
                if avg == node.val:
                    ans[0] += 1
                return v_list
        func(root)
        return ans[0]
        """
        self.ans = 0
        def func(node:TreeNode):
            if node is None:
                return 0,0
            left_sum, left_cnt = func(node.left)
            right_sum, right_cnt = func(node.right)
            total_sum = (node.val + left_sum + right_sum)
            total_cnt = 1 + left_cnt + right_cnt 
            avg = total_sum // total_cnt
            if node.val == avg:
                self.ans += 1
            
            return total_sum, total_cnt
        func(root)
        return self.ans