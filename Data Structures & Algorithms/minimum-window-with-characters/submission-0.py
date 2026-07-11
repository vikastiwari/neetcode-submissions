class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer=""

        freq_map = {}
        window = defaultdict()

        for ch in t:
            freq_map[ch]=freq_map.get(ch,0)+1 

        have = 0
        need = len(freq_map)

        left =0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch,0) + 1

            if ch in freq_map.keys():
                if window[ch] == freq_map.get(ch):
                    have+=1

            while have == need :
                if answer == "" or len(answer)>len(s[left:right+1]):
                    answer= s[left:right+1]

                window[s[left]]-=1

                if s[left] in freq_map.keys():   
                    if window[s[left]] < freq_map.get(s[left]):
                        have-=1   

                left+=1
        return answer