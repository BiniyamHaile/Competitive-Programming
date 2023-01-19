class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = [0 for i in range(k)]
        sum = 0
        for num in nums:
            sum += num%k
            counter[sum%k] +=1
        result = counter[0]
        for res in counter:
            result += res*(res-1) // 2
        return result
    
        