# Last updated: 7/30/2025, 12:23:57 PM
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst= []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lst.append('FizzBuzz')
            elif i%3==0:
                lst.append('Fizz')
            elif i%5==0:
                lst.append('Buzz')
            else:
                lst.append(str(i))
        return lst