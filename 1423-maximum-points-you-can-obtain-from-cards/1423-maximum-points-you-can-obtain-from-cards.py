class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        left = [0]
        right = [0]
        right_idx = len(cardPoints)-1

        for i in range(k):
            left.append(cardPoints[i] + left[-1])
        for j in range(k):
            right.append(cardPoints[right_idx] + right[-1])
            right_idx-=1
        maximum = 0
        right_idx = -1

        for i in range(k+1):
            maximum = max(maximum , left[i] + right[right_idx])
            right_idx -=1
        
        return maximum