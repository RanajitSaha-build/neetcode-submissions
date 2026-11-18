class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using set()
        if len(nums) == len(set(nums)):
            return False
        return True

        
