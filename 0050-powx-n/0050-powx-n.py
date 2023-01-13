class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x  ,n ):
            if n == 0 :
                return 1
            if x == 0 :
                return 0
            result = helper(x , n//2)
            result *= result
            return x*result if n % 2 else result
        
        res = helper(x , abs(n))
        
        return res if n >= 0 else 1/res