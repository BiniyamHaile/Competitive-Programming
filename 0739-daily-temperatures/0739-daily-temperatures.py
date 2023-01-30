class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0 for i in range(len(temperatures))]
        stack = []
        for index  , temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemperature , stackIndex  = stack.pop()
                days[stackIndex] = index - stackIndex
            stack.append([temperature , index])
        return days
            
        