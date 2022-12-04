class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myList = []
        count = 0
        for i in nums:
            for j in range(len(nums)):
                if i > nums[j]:
                    count+=1
            myList.append(count)
            count = 0
        
        return myList
