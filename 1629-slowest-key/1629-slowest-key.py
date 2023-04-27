class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        temp_l = []
        for idx, t in enumerate(releaseTimes):
            if idx == 0:
                temp_l.append(t)
            else:
                #print(f'{t} - {releaseTimes[idx - 1]}')
                temp_l.append(abs(releaseTimes[idx - 1] - t))
        #print(temp_l)
        ans_l = list(zip(temp_l, keysPressed))
        ans_l.sort(key=lambda x: (x[0], x[1]))
        return ans_l[-1][1]
        """
        temp_l = []
        for idx, t in enumerate(releaseTimes):
            temp_l.append(t if idx == 0 else abs(releaseTimes[idx - 1] - t))
        ans_l = list(zip(temp_l, keysPressed))
        ans_l.sort(key=lambda x: (x[0], x[1]))
        return ans_l[-1][1]
        