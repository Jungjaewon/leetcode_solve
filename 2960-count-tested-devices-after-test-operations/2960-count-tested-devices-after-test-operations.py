class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        """
        ans = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0 :
                ans += 1
                for j in range(i + 1, len(batteryPercentages)):
                    if batteryPercentages[j] > 0 :
                        batteryPercentages[j] -= 1
        return ans
        """
        ans = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0 :
                ans += 1
                for j in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return ans
            