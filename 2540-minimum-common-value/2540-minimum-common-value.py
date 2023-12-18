class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        inter_sect = set(nums1).intersection(nums2)
        
        if len(inter_sect) == 0:
            return -1
        else:
            return sorted(list(inter_sect))[0]
        