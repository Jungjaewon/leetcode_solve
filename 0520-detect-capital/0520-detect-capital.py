class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all([w.isupper() for w in word]):
            return True
        if word[0].isupper():
            return all([x is False for x in [w.isupper() for w in word[1:]]])
        if all([w.islower() for w in word]):
            return True
        
        return False
            