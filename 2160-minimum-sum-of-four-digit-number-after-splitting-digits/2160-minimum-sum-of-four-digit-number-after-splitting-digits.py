class Solution:
    def minimumSum(self, num: int) -> int:
        """
        ans, num = [10e4], sorted(str(num))
        def func(num, idxs):
            if len(idxs) >= len(num):
                return
            elif len(idxs):
                print(idxs)
                a = int("".join([num[x] for x,c in enumerate(num) if x in idxs]))
                b = int("".join([num[x] for x,c in enumerate(num) if x not in idxs]))
                #print(a,b)
                ans[0] = min(ans[0], a + b)
            for i in range(len(num)):
                if i not in idxs:
                    idxs.append(i)
                    func(num, idxs)
                    del idxs[-1]
        func(num, [])
        return ans[0]
        """
        ans, num = 10e4, sorted(str(num))
        for k in range(1,3):
            candidates = list(itertools.combinations(list(range(len(num))),k))
            for candi in candidates:
                a = int("".join([num[x] for x in range(len(num)) if x in candi]))
                b = int("".join([num[x] for x in range(len(num)) if x not in candi]))
                ans = min(ans, a + b)
        return ans
        
                            