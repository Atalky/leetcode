"""
5. Longest Palindromic Substring
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/
Tags: String, Dynamic Programming
Date: 2026-09-07
Time Complexity: O(n^2)
Space Complexity: O(1) 
Hints used: non form leetcode but used stackoverflow and ai to understand concepts such as


Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

#Finding the longest palindrome substring within a string s:
# my soltuions

# idea 1; 
# to find the longest palindrome first check if it is a palindrome and if it is - how long is it and then comparing aginst any others found. 
# start at the middle and move outword - 

#idea 2: 
# try checking first and last charcters in string if the same then go in one and check again if all matches ie first and last second first and second last return length but if not first and last 
# then return legnth - non palindrome chracters


# Idea 1: makes the most sense to first check if a planindrome exists and then the longest palindrome within it. 

s1 = "babad"
s2 = "cbbd"
s3 = "42dbbd25"

class Solution(object):
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s):
        best_start, best_end = 0, 0

        for i in range(len(s)):
            start1, end1 = self.expand(s, i, i)          # odd-length, centered on i
            start2, end2 = self.expand(s, i, i + 1)       # even-length, centered between i and i+1

            if end1 - start1 > best_end - best_start:
                best_start, best_end = start1, end1
            if end2 - start2 > best_end - best_start:
                best_start, best_end = start2, end2

        return s[best_start:best_end + 1]

sol = Solution()
print(sol.longestPalindrome(s3))



        
