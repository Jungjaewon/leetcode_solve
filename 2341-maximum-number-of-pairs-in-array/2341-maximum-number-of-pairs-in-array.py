class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        a_dict, ans, ret = defaultdict(int), 0, 0
        for n in nums:
            a_dict[n] += 1
        for n in a_dict:
            ans += a_dict[n] // 2
            a_dict[n] = a_dict[n] % 2
        for n in a_dict:
            ret += a_dict[n]
        return [ans, ret]