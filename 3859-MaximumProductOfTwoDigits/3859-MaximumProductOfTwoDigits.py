# Last updated: 7/30/2025, 11:56:59 AM
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n);
        lst = [int(i) for i in s]
        lst = sorted(lst,reverse=True)
        return lst[1]*lst[0]