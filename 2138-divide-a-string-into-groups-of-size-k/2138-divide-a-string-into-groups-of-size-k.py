class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = list()
        for i in range(0,len(s),k):
            temp = s[i:i+k]
            if len(temp) < k:
                for _ in range(k - len(temp)):
                    temp += fill
            ans.append(temp)
        return ans