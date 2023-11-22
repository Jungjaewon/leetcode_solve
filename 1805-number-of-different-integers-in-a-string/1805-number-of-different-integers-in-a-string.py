class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans, i = set(), 0
        temp = list()
        while i < len(word):
            print(temp)
            if word[i].isalpha():
                if len(temp) > 0:
                    ans.add(int(''.join(temp)))
                    temp = list()
            else:
                temp.append(word[i])
            i +=1
        if len(temp) > 0:
            #print(temp)
            ans.add(int(''.join(temp)))
        print(ans)
        return len(ans)