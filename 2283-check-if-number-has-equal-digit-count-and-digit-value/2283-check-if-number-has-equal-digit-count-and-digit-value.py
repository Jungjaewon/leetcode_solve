class Solution:
    def digitCount(self, num: str) -> bool:
        a_dict = defaultdict(int)
        for c in num:
            a_dict[int(c)] += 1
        for idx, c in enumerate(num):
            if int(c) != a_dict[idx]:
                return False
        return True
            
            
            
        