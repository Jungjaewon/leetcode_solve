class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        ans = -1
        for a, b in list(combinations(nums, 2)):
            if sorted(list(str(a)))[-1] == sorted(list(str(b)))[-1]:
                ans = max(ans, a + b)
        return ans
        """
        """
        ans = -1
        for a, b in list(combinations(nums, 2)):
            if max(list(str(a))) == max(list(str(b))):
                ans = max(ans, a + b)
        return ans
        """
        """
        ans = -1
        a_dict = defaultdict(list)
        for num in nums:
            a_dict[max(list(str(num)))].append(num)
        max_key = sorted(list(a_dict.keys()))[-1]
        for n in a_dict:
            if len(a_dict[n])> 1:
                for a,b in list(combinations(a_dict[n],2)):
                    ans = max(ans, a + b)
        return ans
        """
        """
        ans = -1
        a_dict = defaultdict(list)
        for num in nums:
            a_dict[max(list(str(num)))].append(num)
        max_key = sorted(list(a_dict.keys()))[-1]
        for n in a_dict:
            if len(a_dict[n])> 1:
                sorted_n = sorted(a_dict[n])
                ans = max(ans, sorted_n[-1] + sorted_n[-2])
        return ans
        """
        ans = -1
        a_dict = defaultdict(list)
        for num in nums:
            a_dict[max(list(str(num)))].append(num)
        max_key = sorted(list(a_dict.keys()))[-1]
        for n in a_dict:
            if len(a_dict[n])> 1:
                def find_n(items):
                    if len(items) == 2:
                        return items
                    else:
                        f,s = -1, -1
                        for k in items:
                            if k > f:
                                s = f
                                f = k
                            elif k <= f and k > s:
                                s = k
                        return f,s    
                a,b = find_n(a_dict[n])
                ans = max(ans, a + b)
        return ans
    
    
    
    