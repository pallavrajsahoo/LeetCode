class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        result = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            heapq.heappush(result, (c,n))
            if len(result) > k:
                heapq.heappop(result)
  
        
        final = [i[1] for i in result]
        return final
            
            
        
        