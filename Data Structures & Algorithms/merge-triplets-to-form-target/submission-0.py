class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # We will keep a set of the indices (0, 1, 2) that we have successfully matched
        good_indices = set()
        
        for t in triplets:
            # 1. The Greedy Choice: Is this triplet Toxic?
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # Throw it in the trash!
                
            # 2. It's safe! Let's check if it has any of our target numbers
            if t[0] == target[0]:
                good_indices.add(0)
            if t[1] == target[1]:
                good_indices.add(1)
            if t[2] == target[2]:
                good_indices.add(2)
                
        # 3. Did we successfully find a match for all 3 positions using only safe triplets?
        return len(good_indices) == 3
