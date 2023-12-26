class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        reverse_c = [c for c in s if c.isalpha() ][::-1]
        s_list, idx = list(s), 0
        for i in range(len(s_list)):
            if s_list[i].isalpha():
                s_list[i] = reverse_c[idx]
                idx += 1
        return ''.join(s_list)