class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        lista = [intervals[0]]
        for i in range(1, len(intervals)):
            if lista[-1][1] >= intervals[i][0]:
                lista[-1] = [lista[-1][0] , max(lista[-1][1] , intervals[i][1])]
            else:
                lista.append(intervals[i])
        return lista