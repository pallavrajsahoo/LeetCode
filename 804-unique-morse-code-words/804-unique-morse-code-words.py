class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        val = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d = dict.fromkeys(string.ascii_lowercase, 0)
        i=0
        for key in d:
            d[key] = val[i]
            i+=1
            
        unique = set()
        for word in words:
            size = len(word)
            morse = ''
            for j in range(size):
                morse += d[word[j]]
            
            unique.add(morse)
        
        return len(unique)
            
        