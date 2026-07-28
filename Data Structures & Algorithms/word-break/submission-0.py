class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp dictionary to cache our results
        dp = {}
        
        # We only need ONE pointer 'i' (the start of our current substring)
        def dfs(i):
            # Base Case: We successfully matched words all the way to the end!
            if i == len(s):
                return True
                
            # If we already calculated this index, just return the cached answer
            if i in dp:
                return dp[i]
                
            # Try matching every word in the dictionary starting at index 'i'
            for word in wordDict:
                # Does the slice of the string match the word?
                if s[i : i + len(word)] == word:
                    
                    # It matches! Can the REST of the string be broken down?
                    if dfs(i + len(word)) == True:
                        dp[i] = True
                        return True
                        
            # If no words worked for this index, cache False and return False
            dp[i] = False
            return False
            
        # Start the recursion from the very beginning of the string
        return dfs(0)
