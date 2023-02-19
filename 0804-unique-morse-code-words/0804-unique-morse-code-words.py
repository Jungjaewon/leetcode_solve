class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
                 ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        def convert(c):
            return ord(c) - ord('a')
        
        for word in words:
            transed = list()
            for c in word:
                idx = convert(c)
                transed.append(morse[idx])
            result.add(''.join(transed))
        
        return len(result)
                