from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
       
        freq_s = {}
        freq_t = {}

        for charS,charT in zip(s,t):
            freq_s[charS] = freq_s.get(charS,0) + 1
            freq_t[charT] = freq_t.get(charT,0) + 1

        return freq_s == freq_t 