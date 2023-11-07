class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split()
        ans = list()
        for i in range(len(text_list)):
            if i + 2 < len(text_list) and text_list[i] == first and text_list[i + 1] == second:
                ans.append(text_list[i + 2])
        return ans