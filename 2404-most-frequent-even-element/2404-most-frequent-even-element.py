class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt_list = [[key, item] for key, item in dict(Counter(nums)).items() if key & 1 == 0]
        if len(cnt_list) == 0:
            return -1
        else:
            cnt_list.sort(key=lambda x : (x[1], -x[0]), reverse=True)
            print(cnt_list)
            return cnt_list[0][0]
        