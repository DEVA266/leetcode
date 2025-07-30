# Last updated: 7/30/2025, 12:23:48 PM
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        set1,set2,set3 = set("qwertyuiop") , set("asdfghjkl") , set("zxcvbnm") 
        for word in words:
            wordset = set(word.lower())
            if wordset <= set1 or wordset <= set2 or wordset <= set3 :
                ans.append(word)
        return ans