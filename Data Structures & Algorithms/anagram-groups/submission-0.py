class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for item in strs:
            freq_map = {}

            for char in item:
                freq_map[char] = freq_map.get(char,0) + 1

            key = tuple(sorted(freq_map.items())) 
            answer[key].append(item)   

        return list(answer.values())    
