class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        length = len(nums)
        j = length -1
        i = 0
        count = 0
        while i < j :
            sum = nums[i]+nums[j]
            if sum < k:
                i +=1
            elif sum > k :
                j -=1
            elif sum == k:
                count +=1
                i +=1
                j -=1
        return count
