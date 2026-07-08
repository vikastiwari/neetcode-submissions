class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer=[]
        for index,num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue 

            target=-num
            left=index+1
            right=len(nums)-1

            while(right>left):

                if right==index:
                    right-=1

                if(nums[left]+nums[right]>target):
                    right-=1

                elif (nums[left]+nums[right]<target):
                    left+=1

                else :
                    answer.append([num,nums[left],nums[right]])
                    left+=1

                    while right>left and nums[left]==nums[left-1]:
                        left+=1


        return answer             





        