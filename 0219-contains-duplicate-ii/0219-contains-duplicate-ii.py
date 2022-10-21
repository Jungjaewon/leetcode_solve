class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a_dict = dict()
        for idx, n in enumerate(nums):
            if n not in a_dict:
                a_dict[n] = list()
            a_dict[n].append(idx)
        for n in a_dict:
            if len(a_dict[n]) >= 2:
                result_list = a_dict[n]
                for i in range(len(result_list)):
                    for j in range(i + 1, len(result_list)):
                        if abs(result_list[i] - result_list[j]) <= k:
                            return True    
        return False