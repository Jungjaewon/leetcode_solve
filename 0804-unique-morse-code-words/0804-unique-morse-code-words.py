class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
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
        """
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
                 ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            transed = list()
            for c in word:
                transed.append(morse[ord(c) - ord('a')])
            result.add(''.join(transed))
        return len(result)
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
                 ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({''.join([morse[ord(c) - ord('a')] for c in word]) for word in words })
            
                