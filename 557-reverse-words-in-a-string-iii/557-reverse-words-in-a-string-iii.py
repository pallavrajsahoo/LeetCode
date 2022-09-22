class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split(" ");
        
        result = [str[::-1] for str in result]
        
        return " ".join(result)
            
        