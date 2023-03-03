class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        steps = [-1 for x in range(n+1)]
        return self._solveStairs(n, steps)

    def _solveStairs(self, n, steps):
        if(n <= 2):
            return n

        if(steps[n] != -1):
            return steps[n]
        
        steps[n] = self._solveStairs(n-1, steps)+self._solveStairs(n-2,steps)
        return steps[n] 
    
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))