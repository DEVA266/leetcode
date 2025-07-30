# Last updated: 7/30/2025, 11:57:06 AM
class Solution:
    def isValid(self, word: str) -> bool:
        l = False
        alnum = True
        vowel = False
        cons = False
        # if len(word)>=3:
        #     l = True
        # else :
        #     return False
        l = True if (len(word)>=3) else False

        for i in word :
            if i.lower() in "aeiou" :
                vowel = True
                continue
            elif not(i.isalnum()) :
                alnum = False
                return False
            elif i.isalpha() and (i.lower() not in "aeiou") :
                cons = True
        return l and vowel and alnum and cons
        
        