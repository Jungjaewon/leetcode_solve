class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(f'0b{"".join(["0" if b == "1" else "1" for b in bin(n)[2:]])}',2)