class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a_dict = dict(Counter(nums))
        unique_n = len(a_dict)
        for key, repeated in a_dict.items():
            if repeated == unique_n - 1:
                return key
        """
        unique_n = len(set(nums)) 
        for key, repeated in dict(Counter(nums)).items():
            if repeated == unique_n - 1:
                return key
        """
        