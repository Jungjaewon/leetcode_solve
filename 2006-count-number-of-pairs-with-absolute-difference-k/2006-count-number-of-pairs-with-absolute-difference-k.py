class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans
        """
        # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/1471015/Python-Clean-and-concise.-Dictionary-T.C-O(N)
        # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/2552609/Python-Faster-than-99
        """
        ans, seen = 0, defaultdict(int)
        for n in nums:
            seen[n] += 1
            ans += seen[n - k] + seen[n + k]
        return ans
        """
        """
        arr = [0] * 201
        count = 0
        
        # Put the count of each number in the array above
        for num in nums: 
            arr[num] += 1
        
        # Now for each number, just check how many times (num + k) appears in the array and 
		# increment the counter variable with that value
		# Because for each number, if we have number + k in array, it means that pair has an absolute difference of k
        for num in nums: 
            count += arr[num + k]

        return count
        """
        ans, seen = 0, defaultdict(int)
        for n in nums:
            seen[n] += 1
        for n in nums:
            ans += seen[n + k]
        return ans