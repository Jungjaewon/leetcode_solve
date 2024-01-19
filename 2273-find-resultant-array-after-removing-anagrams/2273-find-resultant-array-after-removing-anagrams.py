class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        while not len(words) == 2:
            for i in range(len(words) - 1):
                if i >= len(words):
                    break
                a_dict = dict(Counter(words[i])) 
                b_dict = dict(Counter(words[i + 1]))
                flag, idx = False, -1
                for key in a_dict:
                    if key not in b_dict:
                        break
                    elif key in b_dict and a_dict[key] != b_dict[key]:
                        break
                    elif key in b_dict and a_dict[key] == b_dict[key]:
                        flag = True
                        idx = i + 1
                        break
                if flag:
                    del words[i + 1]
                break        
        return words
        """
        first_s = True
        while first_s or len([x for x in words if x == -1]) > 0:
            i = 0
            words = [x for x in words if x != -1]
            print(words)
            while i < len(words) - 1:
                flag = True
                if len(words[i]) != len(words[i + 1]):
                    flag = False
                elif sorted(words[i]) != sorted(words[i + 1]):
                    flag = False
                
                if flag:
                    words[i + 1] = -1
                    i += 2
                else:
                    i += 1
            #print(words)
            first_s = False
        return [x for x in words if x != -1]