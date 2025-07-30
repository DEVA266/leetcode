# Last updated: 7/30/2025, 12:23:23 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        excepted = sorted(heights)
        for i in range(len(heights)) :
            if heights[i] != excepted[i]:
                count += 1
        return count

        