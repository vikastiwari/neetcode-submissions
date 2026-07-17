class TrieNode:
    def __init__(self):
        self.dict = [None]*26
        self.finished = False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        dictionary=self.root.dict
        for index,ch in enumerate(word):
            if dictionary[ord(ch)-ord('a')] is None:
                dictionary[ord(ch)-ord('a')]=TrieNode()
            if index==len(word)-1:
                    dictionary[ord(ch)-ord('a')].finished=True     
            dictionary=dictionary[ord(ch)-ord('a')].dict    



    def search(self, word: str) -> bool:
        dictionary=self.root.dict
        for index,ch in enumerate(word):
            if dictionary[ord(ch)-ord('a')] is not None:
                if index==len(word)-1:
                    return dictionary[ord(ch)-ord('a')].finished 
            else:
                return False
            dictionary=dictionary[ord(ch)-ord('a')].dict  
        return True      

        

    def startsWith(self, prefix: str) -> bool:
        dictionary=self.root.dict
        for index,ch in enumerate(prefix):
            if dictionary[ord(ch)-ord('a')] is not None:
                if index==len(prefix)-1:
                    return True 
            else:
                return False
            dictionary=dictionary[ord(ch)-ord('a')].dict  
        return True      

        
        