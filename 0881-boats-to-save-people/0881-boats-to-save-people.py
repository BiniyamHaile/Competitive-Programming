class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        l = 0
        r = len(people)-1
        people.sort()
        count = 0
        while l<=r:
            if l < r : 
                if people[r] + people[l] <= limit:
                    r -=1
                    l+=1
                else:
                    r-=1
            elif l ==r:
                l+=1
                r-=1
            count+=1
        
                
                
                
        return count   
        