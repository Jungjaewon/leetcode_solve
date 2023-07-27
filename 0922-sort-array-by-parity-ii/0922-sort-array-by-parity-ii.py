class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        odd_l, even_l = [n for n in nums if n & 1 == 1], [n for n in nums if n & 1 == 0]
        ans = list()
        odd_cnt, even_cnt = 0,0
        for i in range(len(nums)):
            if i & 1 == 1:
                ans.append(odd_l[odd_cnt])
                odd_cnt += 1
            else:
                ans.append(even_l[even_cnt])
                even_cnt += 1
        return ans
        """
        odd_l, even_l = [n for n in nums if n & 1 == 1], [n for n in nums if n & 1 == 0]
        ans = list()
        for e, o in zip(even_l, odd_l):
            ans.append(e)
            ans.append(o)
        return ans
        