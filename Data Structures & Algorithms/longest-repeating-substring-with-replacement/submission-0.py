class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer=0
        left=0
        window_freq={}

        for right in range(len(s)):


            window_freq[s[right]] = window_freq.get(s[right],0)+1

            while (right-left+1) - max(window_freq.values()) >k :
                window_freq[s[left]]-=1
                left+=1
            if answer < ( right - left + 1 ):
                answer= (right - left + 1)

        return answer    


        