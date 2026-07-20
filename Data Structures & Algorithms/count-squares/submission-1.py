class CountSquares:
    def __init__(self):
        # We need a list to loop through the points, and a map to look up counts instantly
        self.ptsCount = collections.defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        
        # Loop through every single point we've ever added to see if it forms a diagonal
        for x, y in self.pts:
            # 1. To be a square diagonal, the X distance must equal the Y distance!
            # 2. Area cannot be 0, so qx cannot equal x
            if abs(qx - x) == abs(qy - y) and qx != x:
                # We found a diagonal point! Now we just multiply the counts 
                # of where the other two corners MUST mathematically be.
                # If they don't exist, the map returns 0, so res += 0.
                res += self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)]
                
        return res
