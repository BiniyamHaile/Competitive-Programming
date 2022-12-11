class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        myStack = []
        j = 0
        for i in range(len(pushed)):
            myStack.append(pushed[i])
            while len(myStack)>0 and popped[j] == myStack[-1]:
                j+=1
                myStack.pop()

        if len(popped) == j:
            return True
        else :
            return False
