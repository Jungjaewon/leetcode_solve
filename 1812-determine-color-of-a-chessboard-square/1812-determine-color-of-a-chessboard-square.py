class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        x,y = coordinates[0], int(coordinates[1])
        temp = (ord(x) - ord('a')) + 1
        if temp & 1 == 0 and y & 1 == 0:
            return False
        elif temp & 1 == 1 and y & 1 == 0:
            return True
        elif temp & 1 == 0 and y & 1 == 1:
            return True
        elif temp & 1 == 1 and y & 1 == 1:
            return False
        """
        y = int(coordinates[1])
        temp = (ord(coordinates[0]) - ord('a')) + 1
        if temp & 1 == 0 and y & 1 == 0:
            return False
        elif temp & 1 == 1 and y & 1 == 0:
            return True
        elif temp & 1 == 0 and y & 1 == 1:
            return True
        elif temp & 1 == 1 and y & 1 == 1:
            return False
        
        
        