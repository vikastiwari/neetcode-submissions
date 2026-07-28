class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Initialize ALL unique characters with an empty set
        adj = {char: set() for word in words for char in word}
        
        # 2. Build the Adjacency List
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case: If the prefix is identical but w1 is longer, it's invalid!
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break # YOU MUST BREAK HERE!

        # 3. 3-State Cycle Detection DFS
        visit = {} # False = fully visited, True = currently visiting
        answer = []

        def dfs(ch):
            if ch in visit:
                return visit[ch] # Return the boolean, not adj!

            visit[ch] = True    

            for neighbor in adj[ch]:
                if dfs(neighbor):
                    return True # Cycle detected!

            visit[ch] = False
            answer.append(ch) 
            return False

        # 4. Loop through EVERY character in case the graph is disconnected
        for char in adj:
            if dfs(char): # If a cycle is detected anywhere, return ""
                return ""

        # 5. Reverse the list and join into a string!
        return "".join(answer[::-1])
