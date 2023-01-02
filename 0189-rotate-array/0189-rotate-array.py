class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        k = k%length
        l = length - k
        r = length -1
        
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l+=1
            r-=1
        #print(nums)
        l= 0
        r = length - k - 1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l+=1
            r-=1
        #print(nums)
        l = 0
        r = length -1
        
        while l<r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l+=1
            r-=1
        #print(nums)
            
            
        
        