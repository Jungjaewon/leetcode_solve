class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def func(n):
            return sum([1 for i in range(32) if n & 1 << i])
        print(set([func(n) for n in arr]))
        if len(set([func(n) for n in arr])) == 1:
            return sorted(arr)
        else:
            return sorted(arr, key=lambda x : (func(x), x))