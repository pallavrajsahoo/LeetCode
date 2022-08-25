class Solution:
    def romanToInt(self, s: str) -> int:
       
        previous = 0
        result = 0
        
        symbol = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        for i in reversed(s):
            if symbol[i] >= previous:
                previous = symbol[i]
                result += previous
            else:
                previous = symbol[i]
                result -= previous
        
        return result
                
                
            