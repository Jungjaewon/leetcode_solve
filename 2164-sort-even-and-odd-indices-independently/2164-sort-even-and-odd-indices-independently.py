class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_indice, even_indice = list(), list()
        odd_p, even_p = 0,0
        ans = list()
        for idx, n in enumerate(nums):
            if idx & 1: # odd
                odd_indice.append(n)
            else:
                even_indice.append(n)
        
        odd_indice.sort(reverse=True)
        even_indice.sort()
        
        for idx in range(len(nums)):
            if idx & 1:
                ans.append(odd_indice[odd_p])
                odd_p += 1
            else:
                ans.append(even_indice[even_p])
                even_p += 1
        return ans
        