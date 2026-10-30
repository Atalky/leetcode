"""
Problem: 13. Roman to Integer
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/
Tags: Hash Table,Math,String
Date: 2026-10-30
Time Complexity: O(n)
Space Complexity: O(1)
"""

'''
Roman numerals are represented by seven symbols: I, V, X, L, C, D and M.
Usually numerals are written largest to smallest, left to right. The exceptions
are six subtraction cases: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900).
Given a roman numeral, convert it to an integer.
'''


# ---------------------------------------------------------------------------
# My solution: while loop, checking the six special pairs explicitly
# ---------------------------------------------------------------------------
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # go through the input and return each character's value from the dictionary.
        # check if the next element is one of the special cases ie IV or IX, XL or XC, CD or CM.
        # need to check the next term, so loop over the index, not just the character.
        # while loop (not for) because a pair uses two characters, so i sometimes jumps by 2.
        total = 0
        i = 0
        while i < len(s):
            # bounds check first: short-circuiting stops s[i+1] being read past the end
            if i + 1 < len(s) and (
                (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or
                (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or
                (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"))
            ):
                total += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total


# ---------------------------------------------------------------------------
# Optimised: compare values instead of listing the pairs
# Rule: if a numeral is smaller than the one after it, subtract it; otherwise add it.
# e.g. IV -> -1 + 5 = 4, MCM -> 1000 - 100 + 1000 = 1900
# ---------------------------------------------------------------------------
class SolutionOptimised(object):
    def romanToInt(self, s):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        n = len(s)

        for i in range(n):
            current = values[s[i]]
            if i + 1 < n and current < values[s[i + 1]]:
                total -= current
            else:
                total += current

        return total


# ---------------------------------------------------------------------------
# Takeaways
# - Variable step size -> while loop, so you control i yourself.
# - Put the bounds check FIRST inside an `and` (short-circuit protects the risky index).
# - `and` binds tighter than `or`: bracket them whenever you mix them.
# - enumerate(s) gives (index, char) pairs; you can't do char + 1, use s[i + 1].
# - `total += x`, not `total += total + x`.
# - Look for the underlying rule (smaller before larger = subtract) instead of listing special cases.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    for sol in (Solution(), SolutionOptimised()):
        print(sol.romanToInt("III"))      # expect 3
        print(sol.romanToInt("LVIII"))    # expect 58
        print(sol.romanToInt("MCMXCIV"))  # expect 1994
