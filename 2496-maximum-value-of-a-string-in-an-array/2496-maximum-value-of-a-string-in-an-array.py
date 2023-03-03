class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = list()
        for s in strs:
            
            all_alpha = [True for c in s if c.isalpha()]
            all_alpha = False if len(all_alpha) == 0 else all(all_alpha)
            all_digit = [True for c in s if not c.isalpha()]
            all_digit = False if len(all_digit) else all(all_digit)
            print(all_alpha, all_digit)
            if (not all_alpha and all_digit) or all_alpha:
                    ans.append(len(s))
            else:
                ans.append(int(s))
            print(ans)
        return max(ans)