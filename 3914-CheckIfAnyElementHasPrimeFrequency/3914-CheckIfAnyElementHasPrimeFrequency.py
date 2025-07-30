# Last updated: 7/30/2025, 11:56:57 AM
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        for value in set(nums):
            if is_prime(nums.count(value)):
                return True
        return False

