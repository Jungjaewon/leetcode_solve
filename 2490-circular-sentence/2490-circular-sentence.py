class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word_list = sentence.split()
        if len(word_list) == 1:
            return False if word_list[0][0] != word_list[0][-1] else True
        else:
            for idx in range(len(word_list)):
                if idx == 0 and word_list[idx][0] != word_list[len(word_list) - 1][-1]:
                    return False
                elif idx == (len(word_list) - 1) and word_list[idx][-1] != word_list[0][0]:
                    return False
                elif idx + 1 < len(word_list) and word_list[idx][-1] != word_list[idx + 1][0]:
                    return False
        return True