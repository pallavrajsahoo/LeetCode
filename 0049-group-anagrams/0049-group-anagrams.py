class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for each in strs:
            temp = "".join(sorted(each))
            anagrams[temp].append(each)
        
        return anagrams.values()
        
        