class Solution:
    def calPoints(self, operations: List[str]) -> int:
        summation = 0
        myArr = []
        for i in operations:
            if i == "+":
                myArr.append(int(myArr[-2]+myArr[-1]))
                summation+= int(myArr[-1])
            elif i == "D":
                myArr.append(int(myArr[-1] * 2))
                summation+= int(myArr[-1])
            elif i == "C":
                summation -= int(myArr[-1])
                myArr.pop()
            else:
                myArr.append(int(i))
                summation += myArr[-1]
        return summation
                