class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        c = Counter(nums)
        
        for i in c.most_common(k):
            result.append(i[0])
        
        return result
            
        
        