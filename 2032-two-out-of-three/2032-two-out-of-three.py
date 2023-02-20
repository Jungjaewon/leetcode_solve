class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """
        check_dict = defaultdict(int)
        def put_num(num_list):
            for n in set(num_list):
                check_dict[n] += 1
        put_num(nums1)
        put_num(nums2)
        put_num(nums3)
        return [key for key, value in check_dict.items() if value >= 2]
        """
        return list(set(nums1) & set(nums2) | set(nums1) & set(nums3) | set(nums2) & set(nums3))