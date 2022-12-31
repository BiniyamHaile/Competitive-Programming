class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        
        s_idx= 0
        t_idx = 0
        if len(s) ==0 :
            return True
        while t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx+=1
                if s_idx == len(s):
                    return True
            t_idx +=1
            
        return False
                
            
        