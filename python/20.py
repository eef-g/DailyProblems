class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = []
        valid_starts = "({["
        valid_ends = ")}]"
        for c in s:
            if c in valid_starts:
                pars.append(c)
            elif c in valid_ends:
                if len(pars) == 0:
                    return False
                saved = pars[-1]
                if(valid_starts.find(saved) == valid_ends.find(c)):
                    pars.pop()
                else:
                    return False
        if len(pars) == 0:
            return True
        return False 
        
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("()"))
    print(s.isValid("(]"))