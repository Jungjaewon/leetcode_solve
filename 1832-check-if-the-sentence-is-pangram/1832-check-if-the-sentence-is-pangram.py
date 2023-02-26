class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #return len(set(sentence)) == 26
        return len(Counter(sentence)) == 26
        