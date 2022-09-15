class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        return sorted(count, key=count.get, reverse=True)[:k]
        