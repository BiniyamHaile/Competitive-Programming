class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        lista = []
        for i in range(len(nums)):
            if nums[i] == target:
                lista.append(i)
            elif nums[i] > target :
                break
        return lista
