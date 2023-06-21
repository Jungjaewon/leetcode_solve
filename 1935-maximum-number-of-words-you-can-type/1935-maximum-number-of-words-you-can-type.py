class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        ans = 0
        for t in text.split():
            if all([ True if b not in t else False for b in brokenLetters ]):
                ans += 1
        return ans
        """
        ans, letter_set = 0, set(brokenLetters)
        for t in text.split():
            if all([ True if b not in letter_set else False for b in t ]):
                ans += 1
        return ans
        
            
                    
        