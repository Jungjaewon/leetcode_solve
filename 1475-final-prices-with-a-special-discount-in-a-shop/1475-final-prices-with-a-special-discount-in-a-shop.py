class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        ans = list()
        for idx, p in enumerate(prices):
            if idx + 1 == len(prices):
                ans.append(p)
            else:
                dis = None
                for n in prices[idx + 1:]:
                    if p >= n:
                        dis = n
                        break
                ans.append(p - dis if dis is not None else p)
        return ans
        """
        """
        ans = list()
        for idx, p in enumerate(prices):
            if idx + 1 == len(prices):
                ans.append(p)
            else:
                dis = None
                for n in range(idx + 1, len(prices)):
                    if p >= prices[n]:
                        dis = prices[n]
                        break
                ans.append(p - dis if dis is not None else p)
        return ans
        """
        """
        ans = list()
        for idx, p in enumerate(prices):
            dis = None
            for n in range(idx + 1, len(prices)):
                if p >= prices[n]:
                    dis = prices[n]
                    break
            ans.append(p - dis if dis is not None else p)
        return ans
        """
        # https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/discuss/685578/Python-31-pass-O(n)-code-using-stack-w-brief-explanation-and-analysis.
        """
        res, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)
        return res
        """
        i = 0 
        j = i +1

        while i <j and j < len(prices) :
            #STEP 1: INCREASE I TO  NEXT INDEX AND J NEXT TO I IF ITH ELEMENT GREATER THAN JTH AFTER PERFORMING THE OPERATION
            if prices[i] >= prices[j]:
                prices[i] = prices[i] - prices[j]
                i = i +1
                j = i+1
            else:
            #STEP2:  IF THERE IS NO JTH ELEMENT WHICHH IS SMALLER THAN ITH AND YOU REACH END OF ARRAY THEN INCREMENT i and shift back j to i+1
                if (j == len(prices)-1):
                    i = i +1
                    j = i +1

            # STEP3 :ELSE INCREASE j by 1 and re enter in to step 1 if condition satisfies
                else:
                    j = j +1
        return prices
    