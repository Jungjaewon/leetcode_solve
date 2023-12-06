class Solution:
    def makeGood(self, s: str) -> str:
        s_list = list(s)
        while True:
            flag = False
            for i in range(len(s_list) - 1):
                if s_list[i] == -1 or s_list[i + 1] == -1:
                    continue
                elif s_list[i].islower() and s_list[i + 1].islower():
                    continue
                elif s_list[i].isupper() and s_list[i + 1].isupper():
                    continue

                if (s_list[i].lower() == s_list[i + 1]) or (s_list[i] == s_list[i + 1].lower()):
                    s_list[i] = -1
                    s_list[i + 1] = -1
                    flag = True
            s_list = [x for x in s_list if x != -1]
            
            if not flag:
                break
        return ''.join([x for x in s_list if x != -1])