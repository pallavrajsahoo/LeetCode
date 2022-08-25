class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_cnt = Counter(magazine)
        ran_cnt = Counter(ransomNote)
        return ran_cnt & mag_cnt == ran_cnt
        
        