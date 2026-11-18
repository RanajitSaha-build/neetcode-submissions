class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # same thing can be done using Counter 
        from collections import Counter 
        counts = Counter(nums)
        for i in counts:
            if counts[i] > 1:
                return True
        return False
