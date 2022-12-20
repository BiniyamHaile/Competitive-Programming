class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if len(s) == 1:
            return False
        temp = []
        opening = ["(" , "[" , "{"]


        while len(s)>0:
            last_digit = s[-1]
            if last_digit == "}":
                temp.append("{")
            elif last_digit == "]":
                temp.append("[")
            elif last_digit == ")":

                temp.append("(")
            elif last_digit in opening:
                if len(temp) == 0:
                    
                    return False
                elif last_digit == temp[-1]:
                    temp = temp[:-1]
                

                else :
                    
                    return False
            s = s[:-1]
        return len(temp) == len(s)
