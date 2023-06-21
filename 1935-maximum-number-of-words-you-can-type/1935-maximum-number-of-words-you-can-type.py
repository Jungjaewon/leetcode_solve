class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for t in text.split():
            if all([ True if b not in t else False for b in brokenLetters ]):
                ans += 1
        return ans
            
                    
        