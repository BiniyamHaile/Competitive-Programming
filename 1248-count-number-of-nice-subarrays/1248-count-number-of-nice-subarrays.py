class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        table = {0 :1}
        current_sum = 0
        count = 0

        for i in nums:
            current_sum += i % 2
            if current_sum in table:
                table[current_sum] +=1
            else:
                table[current_sum] = 1
            if current_sum - k in table:
                count += table[current_sum-k]

       
        return count
       
        