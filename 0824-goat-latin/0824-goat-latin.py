class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        ans = list()
        for idx, word in enumerate(sentence.split(' ')):
            temp = word
            if temp[0].lower() in vowel:
                temp = f'{temp}ma'
            else:
                temp = f'{temp[1:]}{temp[0]}ma'
            temp = f'{temp}{"a" * (idx + 1)}'
            ans.append(temp)
        return ' '.join(ans)