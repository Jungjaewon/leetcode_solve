class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_func(n : int) -> int:
            s, val = str(n), 0
            for c in s:
                num = int(c)
                val += num * num
            return val
        
        results = list()
        
        
        while True:
            n = get_func(n)
            if n in results:
                return False
            elif n == 1:
                return True
            results.append(n)
        
        return False
        
    # 2 4 16 37 58 89 144 33 18 65 59 106 37
        