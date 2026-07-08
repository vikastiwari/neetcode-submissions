class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer=0
        left=0
        right=len(heights)-1
        
        while right>left:
            vol=(right-left)*min(heights[left],heights[right])
            if(vol>answer):
                answer=vol
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1      
           



        return answer
        