class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        vowel_list = [x for x in s if x.lower() in vowels][::-1]
        v_idx, s_list = 0, list(s)
        for i in range(len(s_list)):
            if s_list[i].lower() in vowels:
                s_list[i] = vowel_list[v_idx]
                v_idx += 1
        return ''.join(s_list)
                
        
        
        