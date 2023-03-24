class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        ans_l, a_dict = list(), defaultdict(int)
        for idx, n in nums1:
            a_dict[idx] += n
        for idx, n in nums2:
            a_dict[idx] +=n
        return [[idx, a_dict[idx]] for idx in sorted(a_dict.keys())]
        """
        a_dict = defaultdict(int)
        for idx, n in nums1:
            a_dict[idx] += n
        for idx, n in nums2:
            a_dict[idx] +=n
        return [[idx, a_dict[idx]] for idx in sorted(a_dict.keys())]
        
        