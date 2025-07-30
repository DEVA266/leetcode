# Last updated: 7/30/2025, 12:24:01 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        values = [ch for ch in magazine]
        for i in ransomNote:
            if i in values:
                values.remove(i)
            else :
                return False
        return True
        