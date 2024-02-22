class RecentCounter:

    def __init__(self):
        self.requests = list()
    def ping(self, t: int) -> int:
        """
        self.requests.append(t)
        return sum([1 for x in self.requests if t - 3000 <= x and x <= t])
        """
        cnt = sum([1 for x in self.requests if t - 3000 <= x and x <= t]) + 1
        self.requests.append(t)
        return cnt
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)