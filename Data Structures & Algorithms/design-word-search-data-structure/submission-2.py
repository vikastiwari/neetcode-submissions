class TrieNode:
    def __init__(self):
        self.dict = collections.defaultdict(TrieNode)
        self.finished=False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        dictionary=self.root.dict
        for index,ch in enumerate(word):
            if ch not in dictionary:
                dictionary[ch]=TrieNode()
            if index==len(word)-1:
                dictionary[ch].finished=True
            dictionary = dictionary[ch].dict    


        

    def search(self, word: str) -> bool:

        def dfs(i,curr_node)->bool:

            if i==len(word):
                return curr_node.finished

            ch=word[i]

            if ch == '.':
                for node in curr_node.dict.values():
                    if dfs(i+1,node):
                        return True
                    
                return False    

            else:
                if ch not in curr_node.dict:
                    return False
                return dfs(i+1,curr_node.dict[ch])        

        return dfs(0,self.root)    


