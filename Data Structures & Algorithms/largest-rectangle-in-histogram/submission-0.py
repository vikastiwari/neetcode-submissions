class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer=0
        stack =[]

        for index,h in enumerate(heights):
            start=index
            while stack and h<stack[-1][0]:
                popped_height, popped_index = stack.pop()
                area = popped_height * (index - popped_index)
                answer=max(answer,area)
                start = popped_index
            
            stack.append([h,start])


        for h,i in stack:
            # The right boundary for these bars is the total length of the array
            area = h * (len(heights) - i)
            answer = max(answer, area)

        return answer
        