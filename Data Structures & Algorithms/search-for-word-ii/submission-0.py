class TrieNode:
    def __init__(self):
        self.dict=collections.defaultdict(TrieNode)
        self.finished=False
        self.index=-1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans=[]
        root=TrieNode()
        dict=root.dict
        # insert words in trie
        for index1,word in enumerate(words):
            dict=root.dict
            for index2,ch in enumerate(word):
                if ch not in dict:
                    dict[ch]=TrieNode()
                if index2==len(word)-1:
                    dict[ch].finished=True
                    dict[ch].index=index1    

                dict=dict[ch].dict    
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c,curr_node):
            if ( r>=ROWS or c>=COLS or r<0 or c<0 or board[r][c] not in curr_node.dict):
                return

            ch = board[r][c]
            curr_node=curr_node.dict[ch]

            if curr_node.finished and curr_node.index!=-1:
                ans.append(words[curr_node.index])
                curr_node.index=-1

            board[r][c]="#"

            dfs(r+1,c,curr_node)
            dfs(r-1,c,curr_node)
            dfs(r,c+1,curr_node)
            dfs(r,c-1,curr_node)
            
            board[r][c]=ch

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)  
        return ans            
        