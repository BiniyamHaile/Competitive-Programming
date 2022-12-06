class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        sum = 0
        max_value = 0 
        nums.sort()
        while end < len(nums):
            sum +=  nums[end]
            while nums[end] * (end -start + 1) > sum + k:
                sum -= nums[start]
                start +=1
            max_value = max(max_value, end-start+1)
            end +=1
        return max_value
