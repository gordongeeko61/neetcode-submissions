class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs1=set()
        for n in nums:
            if n in hs1:
                return True
            hs1.add(n)
        return False 
    
        