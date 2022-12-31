class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        table = {}
        left = 0
        max_fruits = 0 
        
        for end in range(len(fruits)):
            newFruit = fruits[end]
            
            if newFruit in table.keys():
                table[newFruit] +=1
            else:
                table[newFruit] = 1
            
            
            while len(table) > 2:
                leftFruit = fruits[left]
                left+=1
                table[leftFruit] -=1
                if table[leftFruit] == 0:
                    table.pop(leftFruit)
                    
            max_fruits = max(max_fruits , end-left+1)
            
        return max_fruits
        