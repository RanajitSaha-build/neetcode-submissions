class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using dictionary
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
                return True
            else:
                d[i] = 1
        return False

        

        
