class Solution:
    def reverseParentheses(self, s: str) -> str:
        keeper = [""]
        for char in s:
            if char == "(":
                keeper.append("")
            elif char == ")":
                reversed  = keeper.pop()[::-1]
                
                keeper[-1] += reversed
            else:
                keeper[-1] += char
        
            
        
        return keeper[0]
            