class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_dict = defaultdict(int)
        for b in bills:
            print(f' b : {b}, change_dict : {change_dict}')
            if b == 5:
                change_dict[5] += 1
            elif b == 10:
                if change_dict[5] == 0:
                    return False
                else:
                    change_dict[10] += 1
                    change_dict[5] -=1
            elif b == 20:
                if change_dict[10] >= 1 and change_dict[5] >= 1:
                    change_dict[10] -= 1
                    change_dict[5] -= 1
                    change_dict[20] += 1
                elif change_dict[5] >= 3:
                    change_dict[5] -= 3
                    change_dict[20] += 1
                else:
                    return False
        return True