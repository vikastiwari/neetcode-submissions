class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=0
        left=0
        window = set()

        for right in range(len(s)):

            while s[right] in window:
                # move left pointer till our window contains unique elements
                window.remove(s[left])
                left+=1

            else:
                window.add(s[right])

            if answer < (right -left + 1):
                answer = (right -left + 1)

        return answer        
