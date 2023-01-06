class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num = []
        table = {0 :1}
        current_sum = 0
        count = 0
        for i in nums:
            if i%2 != 0:
                num.append(1)
            else:
                num.append(0)
        for i in range(len(nums)):
            current_sum += num[i]
            if current_sum - k in table:
                count += table[current_sum-k]
            if current_sum in table:
                table[current_sum] +=1
            else:
                table[current_sum] = 1

       
        return count