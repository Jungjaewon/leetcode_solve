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
        """
        """
        def get_sum(k):
            return k * (k + 1) // 2
        for idx in range(1, n + 1):
            left_sum = get_sum(idx)
            right_sum = get_sum(n) - left_sum + idx
            if left_sum == right_sum:
                return idx
        return -1
        """
        def get_sum(k):
            return k * (k + 1) // 2
        for idx in range(1, n + 1):
            left_sum = idx * (idx + 1) // 2
            right_sum = n * (n + 1) // 2 - left_sum + idx
            if left_sum == right_sum:
                return idx
        return -1
        
                
                