class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        ans = [0] * len(A)
        for i in range(len(ans)):
            ans[i] = len(set(A[:i + 1]).intersection(set(B[:i + 1])))
        return ans
        """
        a_dict, b_dict = defaultdict(int), defaultdict(int)
        ans = [0] * len(A)
        for i in range(len(ans)):
            a_dict[A[i]] += 1
            b_dict[B[i]] += 1
            cnt = 0
            for key in a_dict:
                if key in b_dict:
                    cnt += 1
            ans[i] = cnt
        
        
        return ans