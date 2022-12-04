class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in points:
            distance = i[0] ** 2 + i[1] ** 2
            i.insert(0 , distance)
        points.sort()
        temp = []
        
 
        for i in range(k):
            temp.append(points[i][1:])
        return temp
