# Last updated: 7/30/2025, 12:23:12 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = {}
        for i in set(arr):
            if int(arr.count(i)) == i :
                m[i] = int(arr.count(i))

        return sorted(m.values() ,reverse=True)[0] if m else -1
        