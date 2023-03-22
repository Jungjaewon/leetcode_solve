class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        return sum([ 1 for word in words[left:right + 1] if word[0] in vowel and word[-1] in vowel])