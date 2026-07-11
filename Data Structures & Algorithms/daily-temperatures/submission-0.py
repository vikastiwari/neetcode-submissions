class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)

        wait = []

        for index,t in enumerate(temperatures):
            while wait and wait[-1][0]<t:
                [popped, pop_index] = wait.pop()
                time = index-pop_index
                answer[pop_index]=time


            wait.append([t,index])
        return answer    
        