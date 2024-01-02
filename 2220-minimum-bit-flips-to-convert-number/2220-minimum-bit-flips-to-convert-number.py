class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #https://leetcode.com/problems/minimum-bit-flips-to-convert-number/discuss/2260588/python-or-easy-or-interview-thinking
        #https://leetcode.com/problems/minimum-bit-flips-to-convert-number/discuss/2379732/One-Liner-Python
        #https://www.educative.io/answers/what-is-kernighans-algorithm
        """
        self.ans = 10e4
        def func(cnt, idx, num, goal):
            if idx == 32:
                return
            elif num == goal:
                self.ans = min(self.ans, cnt)
            else:
                new_num = num & (num ^ (1 << idx))
                func(cnt, idx + 1, num, goal)
                func(cnt + 1, idx + 1, new_num, goal)
        func(0, 0, start, goal)
        return self.ans
        """
        #return (start^goal).bit_count()
        res = start ^ goal
        cnt = 0
        while res:
            res &= res - 1
            cnt += 1
        return cnt