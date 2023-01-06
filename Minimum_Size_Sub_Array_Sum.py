class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        l = 0 
        min_length = len(nums)+1
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                min_length = min(min_length , r - l +1)
                currentSum -= nums[l]
                l+=1
        if min_length  == len(nums)+1:
            return 0

        
        return min_length
