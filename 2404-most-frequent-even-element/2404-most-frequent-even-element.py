class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = []
        for n in nums:
            if n%2 == 0:
                even.append(n)
        
        if len(even) == 0:
            return -1
        
        count = dict()
        for n in even:
            count[n] = 1 + count.get(n, 0)
        
        print(count)
        
        key = float('inf')
        val = 0
        result = 0
        for k, v in count.items():
            if val < v:
                result = k
                val = v
            
            if val == v:
                result = min(result, k)
        
        return result
            
            
                
        