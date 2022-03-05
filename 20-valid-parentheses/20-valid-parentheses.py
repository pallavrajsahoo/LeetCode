class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #check = {')' : '(', ']' : '[', '}' : '{'}
        if len(s) == 1: 
            return False
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
            
        print(stack)
        return len(stack) == 0
            
            
        