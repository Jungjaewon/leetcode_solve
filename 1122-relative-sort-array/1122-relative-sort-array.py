class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt1 = list(), dict(Counter(arr1))
        for n in arr2:
            ans.extend([n] * cnt1[n])
        sub = list()
        for n in arr1:
            if n not in arr2:
                sub.append(n)
        return ans + sorted(sub)