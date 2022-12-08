class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        def reverser(arr , end):
            start = 0
            end -=1
            while start < end:
                arr[start] , arr[end]= arr[end] , arr[start]
                start +=1
                end -=1
    
        def maxIdxFinder(arr , i):
            max_idx = 0
            max_num = 0 
            for i in range(i):
                if  arr[i] > max_num:
                    max_num = arr[i]
                    max_idx = i
            
            return max_idx
        length = len(arr)
        lista = []
        while length  > 1:
            max_idx = maxIdxFinder(arr , length)
           
            reverser(arr , max_idx+1)
            lista.append(max_idx+1)
            reverser(arr , length)
            lista.append(length )
            
            length -=1
         
        return lista
