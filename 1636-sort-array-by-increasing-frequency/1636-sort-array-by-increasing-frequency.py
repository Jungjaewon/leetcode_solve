class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a_dict,ans = defaultdict(int), list()
        for n in nums:
            a_dict[n] += 1
        temp_l = [[n, a_dict[n]] for n in a_dict]
        temp_l = sorted(temp_l, key=lambda x : (x[1], -x[0]) )
        for n, f in temp_l:
            for _ in range(f):
                ans.append(n)
        return ans