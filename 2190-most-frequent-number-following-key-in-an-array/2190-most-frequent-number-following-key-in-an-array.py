class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count_list = list()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                count_list.append(nums[i + 1])
        counter_list = Counter(count_list).items()
        return sorted(counter_list, key= lambda x : -x[1])[0][0]