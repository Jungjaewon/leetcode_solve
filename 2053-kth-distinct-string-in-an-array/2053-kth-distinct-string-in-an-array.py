class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans_list, c = list(), Counter(arr)
        for n in arr:
            if c[n] == 1:
                ans_list.append(n)
        
        print(ans_list)
        if k <= len(ans_list):
            return ans_list[k - 1]
        else:
            return ""