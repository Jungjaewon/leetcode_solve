class Solution:
    def digitCount(self, num: str) -> bool:
        a_dict = defaultdict(int)
        for c in num:
            a_dict[int(c)] += 1
        print(a_dict)
        for idx, c in enumerate(num):
            #print(f'c : {c}, {a_dict[idx]}, idx : {idx}')
            if int(c) != a_dict[idx]:
                return False
        return True
            
            
            
        