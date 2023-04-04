class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        word1_list, word2_list, ans = list(word1), list(word2), list()
        gap = abs(len(word1_list) - len(word2_list))
        for _ in range(gap):
            if len(word1_list) > len(word2_list):
                word2_list.append('*')
            else:
                word1_list.append('*')
        for a,b in zip (word1_list, word2_list):
            ans.append(a)
            ans.append(b)
        return ''.join(ans).replace('*', '')
        """
        word1_list, word2_list, ans = list(word1), list(word2), list()
        gap = abs(len(word1_list) - len(word2_list))
        for _ in range(gap):
            if len(word1_list) > len(word2_list):
                word2_list.append('')
            else:
                word1_list.append('')
        for a,b in zip (word1_list, word2_list):
            ans.append(a)
            ans.append(b)
        return ''.join(ans)