# Last updated: 7/30/2025, 12:23:09 PM
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i,word in enumerate(words):
            for j,w in enumerate(words):
                if i!=j and word in w :
                    ans.append(word)
                    break
        return ans

        