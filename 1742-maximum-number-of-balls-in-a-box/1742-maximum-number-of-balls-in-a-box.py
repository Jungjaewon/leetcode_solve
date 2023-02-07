class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hash_dict = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            key = sum([int(n) for n in str(i)])
            hash_dict[key] += 1
        
        return max([value for key, value in hash_dict.items()])
        