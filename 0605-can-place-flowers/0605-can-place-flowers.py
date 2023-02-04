class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        idx = 0
        def plant(num, index):
            num -= 1
            flowerbed[index] = 1
            return num
        
        while idx < len(flowerbed):
            
            if n == 0:
                break
            
            if flowerbed[idx] == 1:
                pass
            else:
                if 0 < idx - 1 and idx + 1 < len(flowerbed):
                    if flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0:
                         n = plant(n, idx)
                elif idx == 0 and idx + 1 < len(flowerbed) and flowerbed[idx + 1] == 0:
                    n = plant(n , idx)
                elif idx == len(flowerbed) - 1 and flowerbed[idx - 1] == 0:
                    n = plant(n, idx)
            idx += 1
        return True if n == 0 else False