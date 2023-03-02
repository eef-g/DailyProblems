class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev_char = chars[0].lower()
        s = ""
        curr_count = 0
        for c in chars[1:]:
            if c.lower() == prev_char:
                curr_count += 1
            else:
                if curr_count != 0:
                    s += prev_char + str(curr_count + 1)
                else:
                    s += prev_char
                curr_count = 0
            prev_char = c.lower()
        if curr_count != 0:
            s += prev_char + str(curr_count + 1)
        else:
            s += prev_char
        return len(s)
    
if __name__ == "__main__":
    s = Solution()
    test1 = ["a","a","b","b","c","c","c"]
    test2 = ["a"]
    test3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(s.compress(test1))
    print(s.compress(test2))
    print(s.compress(test3))