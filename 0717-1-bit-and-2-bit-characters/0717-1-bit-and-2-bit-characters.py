class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        while len(bits):
            if len(bits) < 2 and bits[0] == 0:
                return True
            elif len(bits) == 2:
                s = f'{bits[0]}{bits[1]}'
                if s in ['10', '11']:
                    return False
                elif s == '00':
                    return True
            else:
                if bits[0] == 0:
                    bits = bits[1:]
                else:
                    s = f'{bits[0]}{bits[1]}'
                    if s in ['10', '11']:
                        bits = bits[2:]
        return True
        """
        while len(bits):
            if len(bits) < 2 and bits[0] == 0:
                return True
            elif len(bits) == 2:
                return True if f'{bits[0]}{bits[1]}' == '00' else False
            else:
                if bits[0] == 0:
                    bits = bits[1:]
                else:
                    if f'{bits[0]}{bits[1]}' in ['10', '11']:
                        bits = bits[2:]
        return True