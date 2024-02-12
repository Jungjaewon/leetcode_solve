class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : -x[-1])
        ans = 0
        for n_b, n_u in boxTypes:
            if truckSize == 0:
                break
            elif truckSize >= n_b:
                truckSize -= n_b
                ans += n_b * n_u
            else:
                ans += truckSize * n_u
                truckSize = 0
        return ans