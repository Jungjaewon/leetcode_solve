class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        #return (arrivalTime + delayedTime) % 24
        return (arrivalTime + delayedTime) if (arrivalTime + delayedTime) < 24 else abs(24 - (arrivalTime + delayedTime)) 