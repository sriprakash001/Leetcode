class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Bubble sort
        # for j in range(len(nums)-1):
        #     for i in range(len(nums)-j-1):
        #         if nums[i] > nums[i+1]:
        #             nums[i+1],nums[i] = nums[i],nums[i+1]

        # Selection sort
        pos = 0
        while pos < len(nums)-1:
            mini = pos
            for i in range(pos+1,len(nums)):
                if nums[i] < nums[mini]:
                    mini = i
            nums[pos],nums[mini] = nums[mini],nums[pos]
            pos += 1
                    



        