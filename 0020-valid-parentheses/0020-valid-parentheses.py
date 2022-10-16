class Solution:
    def isValid(self, s: str) -> bool:
        a, b, c = 0, 0, 0
        stack_l = list()
        for ch in s:
            if ch in ['(', '{', '[']:
                stack_l.append(ch)
            elif ch in [')', '}', ']']:
                if len(stack_l) == 0:
                    return False
                
                if ch == ')':
                    open_c = '('
                elif ch == '}':
                    open_c = '{'
                elif ch == ']':
                    open_c = '['
            
                if stack_l[-1] == open_c:
                    stack_l.pop()
                else:
                    return False
        
        if len(stack_l):
            return False
        
        return True