class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        vowels = ["a" , "e" , "i" , "o" , "u"]
        counter = 0
        max_counter = 0
        idx_list = []
        for r in range(len(s)):
            if r - l + 1 <= k:
                if s[r] in vowels:
                    idx_list.append(r)
                    counter +=1
            else:
                if len(idx_list) >0 and idx_list[0] == l:
                    idx_list.pop(0)
                    counter -=1
                if s[r] in vowels:
                    counter+=1
                    idx_list.append(r)
                l+=1
            
            max_counter = max(max_counter , counter)
        return max_counter                        

