class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"}":"{", ")":"(", "]":"["}
        stack=[]

        for ch in s:
            
            if ch in bracket:
                if stack and stack[-1] == bracket[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
            
        return len(stack) == 0

        