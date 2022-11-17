from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        """
        print(f'nums : {id(nums)}, {nums}') #  140264934162112
        k, temp_l = k % len(nums), deque(nums)
        print(f'temp_l : {id(temp_l)}, {temp_l}')

        while k > 0:
            temp = temp_l.pop()
            temp_l.appendleft(temp)
            k -= 1
        nums = list(temp_l) # 140264934419136
        print(f'nums : {id(nums)}, {nums}')
        """
        """
        k = k % len(nums)
        while k > 0:
            temp = nums[-1]
            del nums[-1]
            nums.insert(0, temp)
            k -= 1
        """
        