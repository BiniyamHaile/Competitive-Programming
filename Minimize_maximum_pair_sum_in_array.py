class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        start = 0
        end = len(nums)-1
        max_num = 0
        while start < end:
            max_num = max(max_num , nums[start]+nums[end])
            start +=1
            end -=1 
        return max_num
