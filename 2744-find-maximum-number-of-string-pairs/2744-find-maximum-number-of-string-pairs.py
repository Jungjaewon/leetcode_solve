class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        """
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    ans += 1
        return ans
        """
        #return sum([1 for i in range(len(words)) for j in range(i + 1, len(words)) if words[i] == words[j][::-1]])
        ans, a_set = 0, set()
        for word in words:
            if word[::-1] in a_set:
                ans += 1
            elif word not in a_set:
                a_set.add(word)
        return ans
            
            
        
        