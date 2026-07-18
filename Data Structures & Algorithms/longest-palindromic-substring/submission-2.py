class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            
            # Scenario 1: ODD length palindromes (Center is one letter, e.g. "aba")
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If this is the longest we have found, save it!
                if (r - l + 1) > resLen:
                    res = s[l : r+1]
                    resLen = r - l + 1
                
                # Expand outwards!
                l -= 1
                r += 1

            # Scenario 2: EVEN length palindromes (Center is BETWEEN letters, e.g. "abba")
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If this is the longest we have found, save it!
                if (r - l + 1) > resLen:
                    res = s[l : r+1]
                    resLen = r - l + 1
                
                # Expand outwards!
                l -= 1
                r += 1
            

        return res
