class Solution:
    def isValid(self, s: str) -> bool:
#         stack = []

#         if len(s) == 1: 
#             return False
#         if s[0] == ')' or s[0] == '}' or s[0] == ']':
#             return False
#         for c in s:
#             if c == '(' or c == '{' or c == '[':
#                 stack.append(c)
#             elif c == ')' and stack and stack[-1] == '(':
#                 stack.pop()
#             elif c == '}' and stack and stack[-1] == '{':
#                 stack.pop()
#             elif c == ']' and stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 return False 
        
#         return len(stack) == 0
          
        stack = []
        check = {'(' : ')', '[' : ']', '{' : '}'}
        for i in s:
            if i in check:
                stack.append(i)
            elif len(stack) == 0 or check[stack.pop()] != i:
                return False
                
        return len(stack) == 0
        
            
            
        