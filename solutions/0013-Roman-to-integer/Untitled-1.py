class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        #solutions:
        #1 takeinput, convert the roman numerals into intgers. and then print the output which should be integer.
        # im going to take the length first, 
        # to do this
        # i need a way to read the input as we move along thorugh each roman numerial. therefore i will  be looking at the  first term 'i'     
        # to check condtionsL is it I X or C followed by V, X ! L, C ! D, M - Repectively. If so then they take a sum off of therwise correct 

        #
        #        reversed_s = s[::-1]
#        print(reversed_s)

        total = 0
        i = 0
        for i in range(len(s)):
            if values[s[i]] == None:
                if values[s[i]] == None and values[s[i]] < values[s[i+1]]:
                    subtract = values[s[i+1]] - values[s[i]]
                    total += subtract
                else:
                    total += values[s[i]] 
            else:
                    total += values[s[i]] 
                


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))        # expect 3
#    print(sol.romanToInt("LVIII"))       # expect 58
 #   print(sol.romanToInt("MCMXCIV"))     # expect 1994

        
        
        
        