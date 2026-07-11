class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        answer=False

        rows = len(matrix)
        cols = len(matrix[0])

        start=0
        end = rows*cols-1

        while end>=start:
            mid=(end+start)//2
            r= mid//cols
            c= mid%cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c]>target:
                end = mid-1
            else :
                start = mid+1        





        return answer
        