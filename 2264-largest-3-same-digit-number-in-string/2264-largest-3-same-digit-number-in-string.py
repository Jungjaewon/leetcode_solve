class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        ans = list()
        for i in range(len(num) - 2):
            temp_s = num[i : i + 3]
            if temp_s[0] == temp_s[1] and temp_s[0] == temp_s[2]:
                ans.append(temp_s)
        if len(ans) > 1:
            ans.sort(key=lambda x : int(x))
            return ans[-1]
        elif len(ans) == 1:
            return ans[0]
        else:
            return ""
        """
        ans = list()
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                ans.append(f'{num[i]}{num[i + 1]}{num[i + 2]}')
        if len(ans) > 1:
            ans.sort(key=lambda x : int(x))
            return ans[-1]
        elif len(ans) == 1:
            return ans[0]
        else:
            return ""