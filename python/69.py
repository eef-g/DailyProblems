class Solution(object):
    def mySqrt(self, n):
        import math
        return int(math.sqrt(n))

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))
