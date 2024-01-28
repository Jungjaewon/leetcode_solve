class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        ans = []
        for i in range(len(temperatures)):
            cnt, flag = 0, False
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    flag = True
                    cnt += 1
                    break
                else:
                    cnt += 1
            ans.append(cnt if flag else 0)
        return ans
        """
        # https://leetcode.com/problems/daily-temperatures/discuss/1574808/C%2B%2BPython-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches
        """
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            cnt, flag = 0, False
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break
        return ans
        """
        ans = [0] * len(temperatures)  # Result array initialized with zeros
        stack = []
        # https://leetcode.com/problems/daily-temperatures/discuss/4630452/24.1-(Approach-1)-or-O(n)-or-Python-and-C%2B%2B(Step-by-step-explanation)
        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                temp_t, temp_i = stack.pop()
                ans[temp_i] = i - temp_i  # Update the result for the popped index
            stack.append([t, i])  # Push the current temperature and its index onto the stack
        return ans  # Return the result array