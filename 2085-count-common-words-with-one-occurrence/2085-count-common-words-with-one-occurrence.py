class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        """
        a_dict, b_dict, ans = defaultdict(int), defaultdict(int), 0
        for w in words1:
            a_dict[w] += 1
        for w in words2:
            b_dict[w] += 1
        for word in a_dict:
            if a_dict[word] == 1:
                if word in b_dict and b_dict[word] == 1:
                    ans += 1
        return ans
        """
        a_dict, b_dict, ans = defaultdict(int), defaultdict(int), 0
        for w in words1:
            a_dict[w] += 1
        for w in words2:
            b_dict[w] += 1
        for word in a_dict:
            if a_dict[word] == 1 and  word in b_dict and b_dict[word] == 1:
                ans += 1
        return ans