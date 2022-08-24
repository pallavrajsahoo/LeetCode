class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        result = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result