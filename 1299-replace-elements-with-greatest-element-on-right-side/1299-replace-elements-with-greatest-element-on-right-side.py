class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        ans = list()
        for idx, n in enumerate(arr):
            temp_l = arr[idx + 1:]
            if len(temp_l):
                #print(temp_l)
                ans.append(max(temp_l))
            else:
                ans.append(-1)
        return ans
        """
        """
        ans = list()
        for idx, n in enumerate(arr):
            max_v = -1
            for v in arr[idx + 1:]:
                max_v = max(v, max_v)
            ans.append(max_v)
        return ans
        """
        ans, max_v = list(), -1
        arr = arr[::-1]
        for idx, n in enumerate(arr):
            if idx == 0:
                ans.append(-1)
            else:
                ans.append(max_v)
            max_v = max(max_v, n)
        return ans[::-1]