class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        a_dict, ans = dict(), [0] * len(score)
        sorted_score = sorted(score)
        for idx, s in enumerate(sorted_score[::-1]):
            if idx + 1 == 1:
                a_dict[s] = "Gold Medal"
            elif idx + 1 == 2:
                a_dict[s] = "Silver Medal"
            elif idx + 1 == 3:
                a_dict[s] = "Bronze Medal"
            else:
                a_dict[s] = str(idx + 1)
        for idx, s in enumerate(score):
            ans[idx] = a_dict[s]
        return ans
        """
        a_dict, ans = dict(), [0] * len(score)
        for idx, s in enumerate(sorted(score)[::-1]):
            if idx + 1 == 1:
                a_dict[s] = "Gold Medal"
            elif idx + 1 == 2:
                a_dict[s] = "Silver Medal"
            elif idx + 1 == 3:
                a_dict[s] = "Bronze Medal"
            else:
                a_dict[s] = str(idx + 1)
        for idx, s in enumerate(score):
            ans[idx] = a_dict[s]
        return ans
        
                