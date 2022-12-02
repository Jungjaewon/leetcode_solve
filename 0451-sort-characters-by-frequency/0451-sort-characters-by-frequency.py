class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        result_cnt, s = Counter(s), ""
        for x in result_cnt.most_common():
            s += x[0] * x[1]
        return s
        """
        from collections import Counter
        result_cnt, s = Counter(s), ""
        for x in result_cnt.most_common():
            for _ in range(x[1]):
                s += x[0]
        return s
        """
        """
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
        """
        