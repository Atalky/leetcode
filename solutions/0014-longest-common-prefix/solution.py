"""
Problem: 14. Longest Common Prefix
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix/
Tags: Array,String,Trie
Date: 2026-11-02
Time Complexity: O(n * m)  n = number of strings, m = length of the longest string
Space Complexity: O(m)     for the output string
"""

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

'''

'''
My solution:
Read the list of strings and compare each of the strings from the first to the last letter, checking if they are the same.
If they are all the same, add the letter to the output string; at the first mismatch, return it.
Use a while loop over the longest string, continuing as long as every string has the same letter at position i.
A word that has run out of letters (i >= len(word)) also counts as a mismatch.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_string = max(strs, key=len)  # returns the longest string in the list
        i = 0
        output = ""
        while i < len(longest_string):
            ch = longest_string[i]
            for word in strs:
                # length check first: short-circuiting stops word[i] being read past the end
                if i >= len(word) or word[i] != ch:  # mismatch found
                    return output
            # only reached if every word matched at position i
            output += ch  # strings have no .append(), so use +=
            i += 1
        return output


# ---------------------------------------------------------------------------
# Takeaways
# - A list already holds separate strings: strs[0], or loop with `for word in strs`.
# - strs[0][2] = character 2 of string 0 (stacked indexing).
# - max(strs, key=len) returns the longest string (plain max() compares alphabetically).
# - Indentation decides what runs per word vs once after all words are checked.
# - Guard with `i >= len(word) or ...` so a shorter word never gets indexed past its end.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))   # expect "fl"
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))      # expect ""
    print(sol.longestCommonPrefix(["flower", "flow"]))             # expect "flow" (shorter word runs out)
    print(sol.longestCommonPrefix([""]))                           # expect ""
