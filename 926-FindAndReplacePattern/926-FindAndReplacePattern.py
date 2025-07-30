# Last updated: 7/30/2025, 12:23:28 PM
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def sol(arg):
            m = {}
            order = []
            for ch in arg :
                if ch not in m :
                    m[ch] = len(m)
                order.append(m[ch])
            return order
        
        patternAns = sol(pattern)
        # for i in words:
        #     wordValue = sol(i)
        #     if patternAns == wordValue:
        #         ans.append(i)
        return [ i for i in words if patternAns == sol(i)]
