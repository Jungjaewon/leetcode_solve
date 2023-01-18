class Solution:
    def sortSentence(self, s: str) -> str:
        split_list = s.split(' ')
        split_list.sort(key= lambda x : int(x[-1]))
        split_list = [x[:-1] for x in split_list]
        return ' '.join(split_list)