class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Stores { number: index }
        
        # enumerate() gives us both the index (i) and the actual value (num)
        for i, num in enumerate(nums):
            complement = target - num
            
            # Checking a key in a dictionary takes O(1) constant time
            if complement in seen:
                return [seen[complement], i]
            # If not found, remember this number and move to the next
            seen[num] = i
            
        return []
