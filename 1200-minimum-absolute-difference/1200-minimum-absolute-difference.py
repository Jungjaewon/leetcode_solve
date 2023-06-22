class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        arr, ans = sorted(arr), list()
        min_gap = abs(arr[1] - arr[0])
        for i in range(1, len(arr) - 1):
            gap = abs(arr[i + 1] - arr[i])
            min_gap = min(gap, min_gap)
            
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) == min_gap:
                ans.append([arr[i], arr[i + 1]])
        return ans
        """
        """
        arr, ans = sorted(arr), list()
        min_gap = abs(arr[1] - arr[0])
        for i in range(1, len(arr) - 1):
            min_gap = min(abs(arr[i + 1] - arr[i]), min_gap)
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) == min_gap:
                ans.append([arr[i], arr[i + 1]])
        return ans
        """
        arr = sorted(arr)
        min_gap = min([ abs(arr[i + 1] - arr[i]) for i in range(len(arr) - 1)])
        return [ [arr[i], arr[i + 1]] for i in range(len(arr) - 1) if abs(arr[i] - arr[i+1]) == min_gap ]
        