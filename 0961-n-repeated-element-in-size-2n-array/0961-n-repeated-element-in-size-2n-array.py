class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        unique_n = len(set(nums)) 
        for key, repeated in dict(Counter(nums)).items():
            if repeated == unique_n - 1:
                return key
        