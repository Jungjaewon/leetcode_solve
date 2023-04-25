class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        ans, temp = 0, 0
        for n in nums:
            if n == 1:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        ans = max(ans, temp)
        return ans
        """
        ans_l, temp = list(), list()
        for n in nums:
            if n == 1:
                temp.append(1)
            else:
                print(len(temp))
                ans_l.append(temp)
                temp = list()
        ans_l.append(temp)
        print([len(x) for x in ans_l])
        return max([len(x) for x in ans_l])