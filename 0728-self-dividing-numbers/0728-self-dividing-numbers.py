class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            check = list()
            for n in str(i):
                if n == '0':
                    check.append(False)
                elif i % int(n) == 0:
                    check.append(True)
            if all(check) and len(str(i)) == len(check):
                ans.append(i)
        return ans
        