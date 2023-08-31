class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            x,y = stones[-2], stones[-1]
            del stones[-1]
            del stones[-1]
            if x < y:
                stones.append(y - x)
        return stones[0] if len(stones) > 0 else 0
            