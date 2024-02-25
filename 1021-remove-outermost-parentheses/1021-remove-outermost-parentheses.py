class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, idx, ans = list(), 0, list()
        ocnt = 0
        while idx < len(s):
            c = s[idx]
            if c == '(':
                stack.append(c)
                ocnt += 1
            elif c == ')':
                ocnt -= 1
                if (len(stack) + 1) % 2 == 0 and ocnt == 0:
                    ans.extend(stack[1:])
                    stack.clear()
                else:
                    stack.append(c)
            #print(stack)
            idx += 1
        return ''.join(ans)