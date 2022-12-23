class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0 
        r = 0
        max_num = 0

        for letter in s:

            if letter not in s[l:r]:
                r +=1

                max_num = max(max_num , r-l)


                if max_num < r-l:
                    print(s[l:r+1])

            elif letter in s[l:r+1]:
                idx = s[l:r+1].find(letter)
                l = idx+1+l
                r+=1
        return(max_num)
            