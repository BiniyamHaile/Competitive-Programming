class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        store = []
        m = 0 
        while m < len(l):
            temp = nums[l[m] : r[m]+1]
            temp.sort()
            print(temp)
            difference = temp[1] - temp[0]
            if len(temp) > 2 :
                for i in range(1 , len(temp) -1):
                    if (temp[i+1] - temp[i] == difference and i == len(temp)-2 ):
                        store.append(True)
                       
                        temp = []
                    elif temp[i+1] - temp[i] != difference :
                        store.append(False)
                       
                        temp = []
                        break

            elif len(temp) ==2 :
            	store.append(True)
            m +=1

        return store
