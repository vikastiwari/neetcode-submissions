class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
            
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        answer = ""
        
        # If key doesn't exist, return ""
        if key not in self.dict:
            return ""
        
        # Grab the list of pairs for this key
        pairs = self.dict[key]
        start = 0
        end = len(pairs) -1

        # Do a Binary Search on the 'pairs' array!

        while start<=end:
            mid = (start+end)//2

            if pairs[mid][1] <= timestamp:
                answer = pairs[mid][0]
                start=mid+1
            
            else:
                end=mid-1
        
        return answer
