class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        ans = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if j == k or i == k:
                        continue
                    #if (digits[i] == digits[j]) or (digits[j] == digits[k]) or (digits[i] == digits[j]):
                    #    continue
                    num = int(f'{digits[i]}{digits[j]}{digits[k]}')
                    if num & 1 == 0:
                        ans.add(num)
        return sorted(list(ans))
        """
        """
        ans = set()
        candis = list(itertools.permutations(digits, 3))
        for x,y,z in candis:
            if x == 0:
                continue
            else:
                s = int(f'{x}{y}{z}')
                if s & 1 == 0:
                    ans.add(s)
        return sorted(list(ans))
        """
        ans = set()
        candis = list(itertools.combinations(digits, 3))
        for x,y,z in candis:
            for i,j,k in list(itertools.permutations([x,y,z],3)):
                if i == 0:
                    continue
                else:
                    s = int(f'{i}{j}{k}')
                    if s & 1 == 0:
                        ans.add(s)
        return sorted(list(ans))