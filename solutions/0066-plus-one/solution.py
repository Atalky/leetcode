"""
Problem: 66. Plus One
Difficulty: Easy
Link: https://leetcode.com/problems/plus-one/
Tags: Array,Math
Date: 2026-11-02
Time Complexity: O(n)
Space Complexity: O(n)
"""

'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # solution: read the list
        # combine the numbers -> then add one and then output as a list
        output = ""
        for value in digits:
            output += str(value)          # strings have no .append(), so use +=
        output = int(output) + 1
        result = [int(c) for c in str(output)]   # list comprehension: each char back to an int
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([4, 3, 2, 1]))   # expect [4, 3, 2, 2]
    print(sol.plusOne([9, 9]))         # expect [1, 0, 0]
    print(sol.plusOne([0]))            # expect [1]

