class TrieNode:
    def __init__(self):
        self.dict = collections.defaultdict(TrieNode)
        self.finished = False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        dictionary=self.root.dict
        for index,ch in enumerate(word):
            if ch not in dictionary:
                dictionary[ch]=TrieNode()
            if index==len(word)-1:
                    dictionary[ch].finished=True     
            dictionary=dictionary[ch].dict    



    def search(self, word: str) -> bool:
        dictionary=self.root.dict
        for index,ch in enumerate(word):
            if ch in dictionary:
                if index==len(word)-1:
                    return dictionary[ch].finished 
            else:
                return False
            dictionary=dictionary[ch].dict  
        return True      

        

    def startsWith(self, prefix: str) -> bool:
        dictionary=self.root.dict
        for index,ch in enumerate(prefix):
            if ch in dictionary:
                if index==len(prefix)-1:
                    return True 
            else:
                return False
            dictionary=dictionary[ch].dict  
        return True      

        
        