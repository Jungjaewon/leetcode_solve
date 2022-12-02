class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        ans_dict, ans = defaultdict(int), list()
        for c in s:
            ans_dict[c] += 1
        temp = list(ans_dict.items())
        temp.sort(key= lambda x : x[1], reverse=True)
        for x in temp:
            for _ in range(x[1]):
                ans.append(x[0])
        return ''.join(ans)
        