class Solution:
    def reformat(self, s: str) -> str:
        
        if len(s) == 1:
            return s
        elif all([True if c.isalpha() else False for c in s]) or all([True if c.isdigit() else False for c in s]):
            return ""
        else:
            alphas = [c for c in s if c.isalpha()]
            digits = [c for c in s if c.isdigit()]
            
            if abs(len(alphas) - len(digits)) >= 2:
                return ""
            
            if len(alphas) > len(digits):
                for _ in range(len(alphas) - len(digits)):
                    digits.append("")
                result = list()
                for a,c in zip(alphas, digits):
                    if a == '' or c == '':
                        result.append(f'{c}{a}')
                        break
                    else:
                        result.append(f'{a}{c}')
                return "".join(result)
            else:
                for _ in range(len(digits) - len(alphas)):
                    alphas.append("")
                result = list()
                for a,c in zip(alphas, digits):
                    if a == '' or c == '':
                        result.append(f'{a}{c}')
                        break
                    else:
                        result.append(f'{c}{a}')
                return "".join(result)