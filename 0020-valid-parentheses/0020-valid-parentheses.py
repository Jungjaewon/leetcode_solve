class Solution:
    def isValid(self, s: str) -> bool:
        a, b, c = 0, 0, 0
        stack_l = list()
        for ch in s:
            
            if ch =='(':
                stack_l.append('(')
            elif ch =='{':
                stack_l.append('{')
            elif ch =='[':
                stack_l.append('[')
                
            elif ch ==')':
                
                if len(stack_l) == 0:
                    return False
                
                if stack_l[-1] == '(':
                    stack_l.pop()
                else:
                    return False
            elif ch =='}':

                if len(stack_l) == 0:
                    return False
                
                if stack_l[-1] == '{':
                    stack_l.pop()
                else:
                    return False
            elif ch == ']':
                
                if len(stack_l) == 0:
                    return False
                
                if stack_l[-1] == '[':
                    stack_l.pop()
                else:
                    return False
        
        if len(stack_l):
            return False
        
        return True