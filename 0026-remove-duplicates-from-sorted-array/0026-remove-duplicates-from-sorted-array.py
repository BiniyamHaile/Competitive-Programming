class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        
        count = 1
        for j in range(1, len(nums)):
            if(nums[i] != nums[j]):
                i +=1
                nums[i] = nums[j]
                j +=1
                count +=1
            else:
                j+=1

        return count
        