class Solution:
    def reorderSpaces(self, text: str) -> str:
        n_space = len([1 for x in text if x == ' '])
        word_list = [ x.strip() for x in text.split(' ') if x != '']
        n_word = len(word_list)
        new_space = int(n_space / (1 if (n_word - 1) == 0 else (n_word - 1)))
        ans = list()
        for idx, word in enumerate(word_list):
            if idx + 1 == len(word_list):
                ans.append(word + ' ' * n_space)
            elif n_space - new_space >= 0:
                ans.append(word + ' ' * new_space)
                n_space -= new_space
            else:
                ans.append(word + ' ' * n_space)
                n_space = 0
        return ''.join(ans)
        