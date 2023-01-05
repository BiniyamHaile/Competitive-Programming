class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0 : 1}
        current_sum = 0 
        count = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum - k in table:
                count += table[current_sum -k]
            if current_sum in table:
                table[current_sum] +=1
            else:
                table[current_sum] = 1

        return count
        