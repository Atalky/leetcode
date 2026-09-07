"""
Problem: 9. Palindrome Number
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/
Tags: Math
Date: 2026-09-07
Time Complexity: O(log10(n))
Space Complexity: O(1)
"""

import math
x1 = 121
x2 = -121
x3 = 10

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 1
        forward = 0
        while forward < len(str(x)) - reverse:
            if str(x)[forward] != str(x)[-reverse:]:
                return False
            forward += 1
            reverse += 1
        return True

isPalindrome = Solution()
print(isPalindrome.isPalindrome(x1))
print(isPalindrome.isPalindrome(x2))
print(isPalindrome.isPalindrome(x3))