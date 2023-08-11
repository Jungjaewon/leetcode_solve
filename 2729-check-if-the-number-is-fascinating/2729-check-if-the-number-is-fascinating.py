class Solution:
    def isFascinating(self, n: int) -> bool:
        a, b = n * 2, n * 3
        c = Counter(str(n) + str(a) + str(b))
        
        for i in range(0, 10):
            if "0" in c:
                return False
            elif '1' <= str(i) and str(i) <= '9':
                if c[str(i)] != 1:
                    return False
        return True
            
                