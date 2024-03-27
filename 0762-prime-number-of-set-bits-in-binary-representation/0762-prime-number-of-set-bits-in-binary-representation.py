class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        def count_set_bit(n):
            cnt = 0
            for i in range(32):
                if n & 1 << i:
                    cnt += 1
            return cnt
        def is_prime(n):
            if n in [0, 1]:
                return False
            for i in range(2,n):
                if n % i == 0:
                    return False
            return True
        for num in range(left, right + 1):
            #print(f'{num}, {count_set_bit(num)}, {is_prime(count_set_bit(num))}')
            if is_prime(count_set_bit(num)):
                ans += 1
        return ans