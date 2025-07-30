# Last updated: 7/30/2025, 12:23:16 PM
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = 0
        for row in grid:
            for i in row :
                if i < 0 :
                    n += 1
        return n
        