class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums).most_common()
        result = []
        for i in range(k):
            result.append(freq[i][0])
        
        return result