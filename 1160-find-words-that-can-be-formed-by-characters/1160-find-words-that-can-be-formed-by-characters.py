class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
        chars_d, ans = dict(Counter(chars)), 0
        for word in words:
            flag = True
            temp_d = dict(Counter(word))
            for c in temp_d:
                if c in chars_d:
                    if not (temp_d[c] <= chars_d[c]):
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                ans += len(word)
        return ans
        """
        """
        chars_d, ans = dict(Counter(chars)), 0
        for word in words:
            flag, temp_d = True, dict(Counter(word))
            for c in temp_d:
                if c in chars_d:
                    if not (temp_d[c] <= chars_d[c]):
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                ans += len(word)
        return ans
        """
        chars_d, ans = Counter(chars), 0
        for word in words:
            flag, temp_d = True, Counter(word)
            for c in temp_d:
                if c in chars_d:
                    if not (temp_d[c] <= chars_d[c]):
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                ans += len(word)
        return ans