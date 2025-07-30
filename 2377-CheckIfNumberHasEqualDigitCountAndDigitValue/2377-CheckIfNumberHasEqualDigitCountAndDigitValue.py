# Last updated: 7/30/2025, 12:22:43 PM
class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
            
        return True



        