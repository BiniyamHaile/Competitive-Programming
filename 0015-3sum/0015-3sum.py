class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lista = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    lista.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
                elif sum > 0 : 
                    r -=1
                elif sum < 0:
                    l +=1
        return lista
                    
                