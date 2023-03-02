class Solution(object):
    def myPow(self, x, n):
        import math as m
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return m.pow(x, n)
    
if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2, 10))