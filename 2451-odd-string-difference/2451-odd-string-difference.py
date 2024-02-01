class Solution:
    def oddString(self, words: List[str]) -> str:
        ans_d = defaultdict(list)
        for word in words:
            temp_list = [0] * (len(word) - 1)
            for i in range(len(word) - 1):
                temp_list.append(ord(word[i + 1]) - ord(word[i]))
            ans_d[str(temp_list)].append(word)
        for key, value in ans_d.items():
            if len(value) == 1:
                return value[0]
        
        
        