class Solution:
    def isFascinating(self, n: int) -> bool:
        """
        a, b = n * 2, n * 3
        c = Counter(str(n) + str(a) + str(b))
        for i in range(0, 10):
            if "0" in c:
                return False
            elif '1' <= str(i) and str(i) <= '9':
                if c[str(i)] != 1:
                    return False
        return True
        """
        """
        c = Counter(str(n) + str(n * 2) + str(n * 3))
        for i in range(0, 10):
            if "0" in c:
                return False
            elif '1' <= str(i) and str(i) <= '9':
                if c[str(i)] != 1:
                    return False
        return True
        """
        """
        c = Counter(str(n) + str(n * 2) + str(n * 3))
        for i in range(0, 10):
            i = str(i)
            if "0" in c:
                return False
            elif '1' <= i and i <= '9':
                if c[i] != 1:
                    return False
        return True
        """
        a = str(n) + str(n * 2) + str(n * 3)
        if '0' in a:
            return False
        if len(a) != len(set(a)):
            return False
        return sum([int(x) for x in a]) == 45
        
        