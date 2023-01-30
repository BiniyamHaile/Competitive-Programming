class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num1 in nums1:
            idx = nums2.index(num1)
            
            if idx == len(nums2)-1:
                output.append(-1)
                
            else: 
                for i in range(idx+1 , len(nums2)):
                        if nums2[i] > num1:
                            output.append(nums2[i])
                            break
                        elif i == len(nums2)-1:
                            output.append(-1)
                    
        return output
        