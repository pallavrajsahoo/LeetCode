class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
         
        return heapq.nlargest(k, freq.keys(), key = freq.get)
        