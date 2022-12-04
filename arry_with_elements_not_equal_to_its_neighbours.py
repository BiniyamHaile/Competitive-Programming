class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        temp = []
        length = len(nums)
        for i in range(0, len(nums)// 2 ):
            temp.append(nums[i])
            temp.append(nums[len(nums)-i-1])
        if length % 2 :
            temp.append(nums[int(length/2)])
        return temp
