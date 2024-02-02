class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                sub_s = s[start + 1:end]
                return len(sub_s)
            else:
                start += 1
                end -= 1
        return -1
        """
        a_dict = defaultdict(list)
        for idx, c in enumerate(s):
            a_dict[c].append(idx)
        ans = - 1
        #print(a_dict)
        for c in a_dict:
            if len(a_dict[c]) >= 2:
                idx_list = sorted(a_dict[c])
                f = idx_list[0]
                e = idx_list[-1]
                ans = max(ans,len(s[f + 1: e]))
        return ans
        