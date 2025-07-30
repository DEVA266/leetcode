# Last updated: 7/30/2025, 12:25:05 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sample = strs[0]
        length = len(sample)
        for i in strs[1:]:
            while sample != i[0:length]:
                length -=1
                if length == 0:
                    return ""
                sample = sample[0:length]
        return sample
