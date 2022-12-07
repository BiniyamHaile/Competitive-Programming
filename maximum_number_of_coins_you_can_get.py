class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        length = len(piles)
        Bob = 0
        Me = length -2
        sum = 0
        while Me > Bob :
        	print(piles[Me])
        	sum += piles[Me]
        	Me -=2
        	Bob +=1
        return sum
