class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cnt, idx, ans = 1, 0, [0] * num_people
        while candies:
            ans[idx] += cnt
            candies -= cnt
            if cnt + 1 <= candies:
                cnt += 1
            else:
                cnt = candies
            if idx + 1 == len(ans):
                idx = 0
            else:
                idx += 1
        print(ans)
        return ans