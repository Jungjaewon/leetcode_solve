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
        """
        """
        word1_list, word2_list, ans = list(word1), list(word2), list()
        for _ in range(abs(len(word1_list) - len(word2_list))):
            if len(word1_list) > len(word2_list):
                word2_list.append('')
            else:
                word1_list.append('')
        for a,b in zip (word1_list, word2_list):
            ans.append(a)
            ans.append(b)
        return ''.join(ans)
        """
        word1_list, word2_list, ans = list(word1), list(word2), list()
        if len(word1_list) >= len(word2_list):
            ret = word1_list[len(word2_list):]
            word1_list = word1_list[:len(word2_list)]
        else:
            ret = word2_list[len(word1_list):]
            word2_list = word2_list[:len(word1_list)]
        for a,b in zip(word1_list, word2_list):
            ans.append(a + b)
        print(ans)
        print(ret)
        return ''.join(ans) + (''.join(ret) if len(ret) else '')
        
        