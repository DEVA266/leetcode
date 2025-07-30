# Last updated: 7/30/2025, 12:23:45 PM
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedValues = sorted(score,reverse=True)
        rankValues = {sortedValues[i] : str(i+1) for i in range(len(score))}
        rankValues[sortedValues[0]] = "Gold Medal"
        if len(score) > 1:
            rankValues[sortedValues[1]] = "Silver Medal"
        if len(score) > 2 :
            rankValues[sortedValues[2]] = "Bronze Medal"
        return [rankValues[i]  for i in score]