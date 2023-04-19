class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1,  cnt2 = dict(Counter(nums1)), dict(Counter(nums2))
        ans_l = list()
        for n in cnt1:
            if n in cnt2:
                for _ in range(min(cnt1[n], cnt2[n])):
                    ans_l.append(n)
        return ans_l
        