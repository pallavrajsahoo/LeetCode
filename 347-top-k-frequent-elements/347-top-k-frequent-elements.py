class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        c = Counter(nums)
        temp = c.most_common(k)
        
        for i in temp:
            result.append(i[0])
        
        #print(result)
        
        return result
            
        
        