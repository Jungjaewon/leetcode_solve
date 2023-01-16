class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans_list = [[name, height] for name, height in zip(names, heights)]
        ans_list.sort(key=lambda x:x[1], reverse=True)
        return [x[0] for x in ans_list]