class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) ==1:

            return 0

        totalSum = 0
        leftSum = 0
        rightSum = 0
        for j in range(len(nums)):
            totalSum += nums[j]

        for i in range(0 , len(nums)):
            if i > 0:
                leftSum += nums[i-1]
            rightSum = totalSum - leftSum - nums[i]
            if rightSum == leftSum: 

                return i


        return -1