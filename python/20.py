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
        
                

# private bool CheckParenthesis(string equation = "( 1 + 1 )")
 
# {
 
#    // This function creates a stack and then uses it to check the parenthesis and formatting of an equation
 
#    MyStack<string> stack = new MyStack<string>();
 
#    // Need to have space between each item in the string for function to work, do not know how to do substrings yet :|
 
#    string[] parts = equation.Split(' ');
 
#   string validStarts = "([{";
#   string validEnds = ")]}";
 
#    foreach (string s in parts)
 
#   {
 
# if (validStarts.Contains(s)
# )
 
# { stack.Push(s); }
 
# else if (validEnds.Contains(s)
# )
 
# {
 
# string saved = stack.Pop();
# if (validStarts.IndexOf(saved) != validEnds.IndexOf(s)
# )
 
# {
 
# return false;
 
# }
 
# }
 
# }
 
# if (stack.isEmpty()
# ) { return true; }
 
# else { return false; }
 
# }