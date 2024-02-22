class RecentCounter:

    def __init__(self):
        self.requests = list()
        from collections import deque
        self.q = deque()
    def ping(self, t: int) -> int:
        """
        self.requests.append(t)
        return sum([1 for x in self.requests if t - 3000 <= x and x <= t])
        """
        """
        cnt = sum([1 for x in self.requests if t - 3000 <= x and x <= t]) + 1
        self.requests.append(t)
        return cnt
        """
        #cnt = len([1 for x in self.requests if t - 3000 <= x and x <= t]) + 1
        #self.requests.append(t)
        #return cnt
        
        self.q.append(t)
        
        while t - self.q[0] > 3000:
            self.q.popleft()
            
        return len(self.q)
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)