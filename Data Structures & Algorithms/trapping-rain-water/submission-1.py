class Solution:
    def trap(self, height: List[int]) -> int:
        answer=0

        left=0
        right=len(height)-1
        max_left=height[left]
        max_right=height[right]

        while left<right:
            
            if(max_left<max_right):
                left+=1
                if(max_left<height[left]):
                    max_left=height[left]

                answer+= max_left-height[left]   

            else:
                right-=1
                if(max_right<height[right]):
                    max_right=height[right]

                answer+= max_right-height[right] 

        return answer             

                    


        