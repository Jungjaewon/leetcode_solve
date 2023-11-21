class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        msb_i = -1
        for i in range(31,-1,-1):
            check = n & (1 << i)
            #print(check, end='')
            if check:
                msb_i = i
                break
        #print()
        #print(f'msb_i : {msb_i}')
        for i in range(msb_i):
            i_bit = (n >> i) & 1
            i_p_bit = (n >> i + 1) & 1
            if i_bit == i_p_bit:
                return False
        return True