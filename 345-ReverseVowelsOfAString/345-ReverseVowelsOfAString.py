# Last updated: 7/30/2025, 12:24:08 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = list("aeiouAEIOU")
        a,b = 0,len(s)-1
        while a<b:
            if s[a] not in vowels:
                a+=1
            elif s[b] not in vowels :
                b-=1
            else :
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
        return "".join(s)