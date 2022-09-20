class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        top_k = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        top_k = sorted(count, key=count.get, reverse=True)[:k]
        return top_k
        