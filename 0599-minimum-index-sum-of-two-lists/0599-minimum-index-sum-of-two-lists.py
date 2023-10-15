class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a_dict, b_dict = dict(), dict()
        ans = list()
        for i, s in enumerate(list1):
            a_dict[s] = i
        for i, s in enumerate(list2):
            b_dict[s] = i
        for s in a_dict:
            if s in b_dict:
                ans.append([s, a_dict[s] + b_dict[s]])
        ans.sort(key=lambda x : x[1])
        return [ x[0] for x in ans  if x[1] == ans[0][1]]