class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans, temp = [first], first
        for e in encoded:
            result = e ^ temp
            ans.append(result)
            temp = result
        #print(ans)
        return ans