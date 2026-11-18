class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word = min(strs, key = len) # min len string
        while len(min_len_word) > 0:
            is_valid = True
            for word in strs:
                # if min_len_word != word[:len(min_len_word)]:
                if not word.startswith(min_len_word):
                    min_len_word = min_len_word[:-1]
                    is_valid = False
                    break
            if is_valid:
                return min_len_word
        return min_len_word