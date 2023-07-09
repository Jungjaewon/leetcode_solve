class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        num_l = list(range(1, n + 1))
        if len(num_l) == 1:
            return n
        else:
            for idx in range(len(num_l)):
                if sum(num_l[:idx + 1]) == sum(num_l[idx:]):
                    return num_l[idx]
            return -1
        """
        num_l = list(range(1, n + 1))
        if len(num_l) == 1:
            return n
        else:
            a,b, cnt = sum(num_l), 0, n
            while cnt > 0:
                if a == b +  cnt:
                    return cnt
                else:
                    #print(a,b, cnt)
                    a, b = a - cnt, b + cnt
                    cnt -= 1
            return -1
        
                
                