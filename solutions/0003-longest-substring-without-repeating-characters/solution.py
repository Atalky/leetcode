"""
Problem: 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Tags: Hash Table,String,Sliding Window
Date: 2026-09-07
Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""

import string
import random 


def id_generator(size=20, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

s = id_generator()
print(s)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            seen[c] = i
            longest = max(longest, i - start + 1)
        return longest

    

sol = Solution()
print(sol.lengthOfLongestSubstring(s))

