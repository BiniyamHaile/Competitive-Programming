class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s



       
        temp = s.split(" ")
        storer = [""] * len(temp)
        temp_string = ""

        for letter in temp :
            idx = int(letter[-1] ) -1
            storer[idx] = letter[ : -1 ]

        for i in range(len(storer)):
            letter = storer[i]
            if i == len(storer)-1:
                temp_string += letter
            else:
                temp_string +=(letter + " ")
             
        return temp_string
        
   
