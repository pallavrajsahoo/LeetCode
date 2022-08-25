class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums).most_common()
        for i in range(k):
            result.append(count[i][0])
            
        return result