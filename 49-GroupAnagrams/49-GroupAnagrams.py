# Last updated: 7/30/2025, 12:24:53 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            sorted_i = " ".join(sorted(i))
            ans[sorted_i].append(i)
        return list(ans.values())
