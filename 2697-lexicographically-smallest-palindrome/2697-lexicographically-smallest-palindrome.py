class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        s, e = 0, len(s_list) - 1
        while s < e:
            if s_list[s] != s_list[e]:
                if s_list[s] < s_list[e]:
                    s_list[e] = s_list[s]
                else:
                    s_list[s] = s_list[e]
            s += 1
            e -= 1
        return ''.join(s_list)
    #https://leetcode.com/problems/lexicographically-smallest-palindrome/discuss/3547083/Python3-Two-Lines-Use-Smaller-characters