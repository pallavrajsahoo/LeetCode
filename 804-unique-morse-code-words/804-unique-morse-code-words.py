class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        val = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformation = set()
        for word in words:
            morse = ''
            for letter in word:
                morse += val[ord(letter)-ord('a')]
            
            transformation.add(morse)
        
        return len(transformation)
        
        
            
        