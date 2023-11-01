class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for oper in operations:
            
            if oper == '+':
                ans.append(ans[-1] + ans[-2])
            elif oper == 'C':
                del ans[-1]
            elif oper == 'D':
                ans.append(ans[-1] * 2)
            else:
                ans.append(int(oper))
        return sum(ans)