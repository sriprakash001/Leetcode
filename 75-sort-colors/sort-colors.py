class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Bubble sort
        # for j in range(len(nums)-1):
        #     for i in range(len(nums)-j-1):
        #         if nums[i] > nums[i+1]:
        #             nums[i+1],nums[i] = nums[i],nums[i+1]

        # Selection sort
        # pos = 0
        # while pos < len(nums)-1:
        #     mini = pos
        #     for i in range(pos+1,len(nums)):
        #         if nums[i] < nums[mini]:
        #             mini = i
        #     nums[pos],nums[mini] = nums[mini],nums[pos]
        #     pos += 1
        
        # Merge sort:
        
        # split the nums
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            self.sortColors(left)
            self.sortColors(right)

            # Pointers
            lp = 0
            rp = 0
            fp = 0

            while lp < len(left) and rp < len(right):
                if left[lp] < right[rp]:
                    nums[fp] = left[lp]
                    lp += 1
                else:
                    nums[fp] = right[rp]
                    rp += 1
                fp += 1
            
            while lp < len(left):
                nums[fp] = left[lp]
                lp += 1
                fp += 1
            
            while rp < len(right):
                nums[fp] = right[rp]
                rp += 1
                fp += 1



                    



        