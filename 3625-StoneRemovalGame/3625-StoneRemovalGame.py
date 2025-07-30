# Last updated: 7/30/2025, 11:56:56 AM
class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 10
        aliceTurn = True
        while (n>=0):
            n -= turn
            turn -= 1
            aliceTurn = not aliceTurn
        return aliceTurn
            
