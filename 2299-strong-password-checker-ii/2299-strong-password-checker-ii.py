class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False
        
        if not (sum([ 1 for c in password if c.islower()]) >= 1):
            return False
        
        if not (sum([ 1 for c in password if c.isupper()]) >= 1):
            return False
        
        if not (sum([ 1 for c in password if c.isdigit()]) >= 1):
            return False
        
        if not (sum([ 1 for c in password if c in "!@#$%^&*()-+"]) >= 1):
            return False
        
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        
        return True