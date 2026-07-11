class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Always binary search on the smaller array
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        total = len(A) + len(B)
        half = total // 2
        
        start = 0
        end = len(A)
        
        while True:
            # i is our cut in A, j is our forced cut in B
            i = (start + end) // 2
            j = half - i
            
            # 2. Get the 4 edge numbers right around the cuts
            A_left = A[i - 1] if i > 0 else float("-infinity")
            A_right = A[i] if i < len(A) else float("infinity")
            
            B_left = B[j - 1] if j > 0 else float("-infinity")
            B_right = B[j] if j < len(B) else float("infinity")
            
            # 3. Check if the cut is perfect!
            if A_left <= B_right and B_left <= A_right:
                # ODD total length
                if total % 2 != 0:
                    return float(min(A_right, B_right))
                # EVEN total length
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                    
            # 4. We took too many big numbers from A. Move cut left!
            elif A_left > B_right:
                end = i - 1
            # We didn't take enough numbers from A. Move cut right!
            else:
                start = i + 1
