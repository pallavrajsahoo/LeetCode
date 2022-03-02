class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        
        for idx, val in enumerate(nums):
            if val in hashmap and idx - hashmap[val] <= k:
                return True
            else:
                hashmap[val] = idx
                
        return False
                
        