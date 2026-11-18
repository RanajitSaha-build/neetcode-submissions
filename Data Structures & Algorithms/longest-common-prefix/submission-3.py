class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word = min(strs, key = len) # min len string
        # min(nums) # gives minimum number
        # min_len_word = use sort and take first element

        for _ in range(len(min_len_word)):
            for word in strs:
                # if min_len_word != word[:len(min_len_word)]:
                if not word.startswith(min_len_word):
                    min_len_word = min_len_word[:-1]
                    break
        return min_len_word