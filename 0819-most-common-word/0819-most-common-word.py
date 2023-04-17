class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        para_dict = dict(Counter(paragraph.lower().split(' ')))
        if '' in para_dict: 
            del para_dict['']
        for b in banned:
            if b in para_dict:
                del para_dict[b]
        para_list = [[key, para_dict[key]] for key in para_dict]
        para_list.sort(key=lambda x : -x[-1])
        return para_list[0][0]
        
        
        