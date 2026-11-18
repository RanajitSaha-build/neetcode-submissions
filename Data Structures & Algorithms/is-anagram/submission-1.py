def manual_counter(s):
    d = dict()
    for i in s:
        d[i] = d.get(i,0) + 1
    return d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return manual_counter(s) == manual_counter(t)