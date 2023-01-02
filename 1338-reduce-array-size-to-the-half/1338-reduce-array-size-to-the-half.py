class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        sum = 0 
        length = len(arr)

        c = Counter(arr)

        sortDict = dict(sorted(c.items() , key = lambda x : x[1] , reverse = True))

        for key , value in sortDict.items() :
            

            count +=1
            
            while value > 0:
                value -=1
                sum +=1
                print("sum : " , sum )
                if sum >= length/2 :
                    print("answer: " , count)

                    return count 
        