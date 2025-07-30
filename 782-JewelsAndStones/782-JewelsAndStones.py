# Last updated: 7/30/2025, 12:23:33 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for i in jewels:
            if i in stones:
                total += int(stones.count(i))
        return total