class Solution:
    def divisorGame(self, n: int) -> bool:
        def func(n):
            picked = -1
            for x in range(1, n):
                if n % x == 0:
                    picked = x
                    break
            if picked == -1:
                return False
            else:
                return picked
        
        a_turn = True
        
        while True:
            result = func(n)
            if result is False:
                if a_turn:
                    return False
                else:
                    return True
            else:
                n = n - result
            
            a_turn = not a_turn
                
                    
                    