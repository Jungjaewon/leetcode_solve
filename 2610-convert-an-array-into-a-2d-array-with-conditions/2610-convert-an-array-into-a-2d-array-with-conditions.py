class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        a_dict, ans = dict(Counter(nums)), list()
        while True:
            flag = True
            for key in a_dict:
                if a_dict[key] != 0:
                    flag = False
                    break
            if flag:
                break
            temp_list = list()
            for key in a_dict:
                if a_dict[key] > 0:
                    a_dict[key] -= 1
                    temp_list.append(key)
            ans.append(temp_list)
        return ans
        