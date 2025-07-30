# Last updated: 7/30/2025, 12:22:51 PM
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = ""
        ans = []
        start = 0
        last = start + k
        while(last<=len(s)):
            ans.append(s[start:last])
            start,last = last,last+k
        if start == len(s):
            return ans
        n += s[start:]
        for i in range(last-len(s)):
            n += fill
        ans.append(n)
        return ans
        
        