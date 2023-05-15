class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_dict = { key : value for key, value in dict(Counter(s1.split(' '))).items() if value == 1}
        s2_dict = { key : value for key, value in dict(Counter(s2.split(' '))).items() if value == 1}
        print(s1_dict)
        print(s2_dict)
        ans = set()
        for key in s1_dict:
            if key not in s2.split(' '):
                ans.add(key)
        for key in s2_dict:
            if key not in s1.split(' '):
                ans.add(key)
        return list(ans)