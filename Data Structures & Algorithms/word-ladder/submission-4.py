class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        # 1. Build the Pattern Dictionary (The Hack!)
        # This prevents us from ever needing to do the slow O(N^2) character comparisons
        wordList.append(beginWord)
        nei = collections.defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
                
        # 2. Setup the BFS
        visit = set([beginWord])
        queue = collections.deque([beginWord])
        res = 1 # We start at level 1
        
        # 3. Run the BFS (Water rippling outwards)
        while queue:
            # We must process the entire level before incrementing `res`
            for i in range(len(queue)):
                word = queue.popleft()
                
                # Did the water touch the exit?!
                if word == endWord:
                    return res
                    
                # Find all neighbors using our fast pattern dictionary
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
                            
            # We finished a full level of BFS, so we took 1 step forward
            res += 1
            
        return 0
