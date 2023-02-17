class Solution:
    def freqAlphabets(self, s: str) -> str:
        a_dict = dict()
        for i in range(97, 123):
            key = ord(chr(i + 1)) - ord('a')
            a_dict[f'{key}' if key < 10 else f'{key}#'] = chr(i)
        
        key_list = [f'{i}#' for i in range(26, 9, -1)]
        key_list.extend([f'{i}' for i in range(9, 0, -1)])
        for key in key_list:
            s = s.replace(key, a_dict[key])
        return s
            
        