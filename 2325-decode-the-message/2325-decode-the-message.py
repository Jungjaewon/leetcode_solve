class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_dict, cnt = {' ' : ' '}, 0
        for c in key:
            if c not in decode_dict:
                decode_dict[c] = chr(97 + cnt)
                cnt += 1
        return ''.join([ decode_dict[m] for m in list(message)])
        
        