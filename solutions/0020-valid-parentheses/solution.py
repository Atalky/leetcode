"""
Problem: 20. Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/
Tags: String,Stack
Date: 2026-11-03
Time Complexity: O(n)  each character is pushed/popped at most once
Space Complexity: O(n)  the pile can hold every character if they're all openers
"""

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

'''

'''
My solution:
First idea was comparing each bracket with the one next to it (or the mirrored one from the end),
but that breaks on nested brackets like "([])" mixed with side-by-side ones like "()(())".
Instead, read the string left to right and keep a pile (stack) of openers that haven't been closed yet.
Opener -> add it to the pile.
Closer -> the pile can't be empty, and the top of the pile must be the opener it closes; pop it off.
At the end the pile must be empty, otherwise something was never closed.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"(": ")", "[": "]", "{": "}"}  # opener (key) -> closer it needs (value)
        pile = []
        for c in s:
            if c in pairs:          # `in` checks keys, so this means c is an opener
                pile.append(c)
            else:
                if len(pile) == 0:  # closer with nothing open
                    return False
                top = pile.pop()    # most recent unclosed opener
                if pairs[top] != c: # closer it needs vs closer we got
                    return False
        return len(pile) == 0       # leftovers mean something was never closed


# ---------------------------------------------------------------------------
# Takeaways
# - == only checks if two characters are identical: '(' == ')' is False.
# - pairs[key] returns the value; lookups only go key -> value, pairs[")"] is a KeyError.
# - `c in pairs` checks keys, not values.
# - Stack (last in, first out): list.append() adds to the top, list.pop() removes and returns it, list[-1] peeks.
# - Negative indexing counts from the end: s[-1] is the last character.
# - return ends the whole function, so a return True inside a loop stops after one check.
# - Compare neighbours only works for side-by-side pairs; nesting needs a stack.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))       # expect True
    print(sol.isValid("()[]{}"))   # expect True
    print(sol.isValid("(]"))       # expect False
    print(sol.isValid("([])"))     # expect True
    print(sol.isValid("([)]"))     # expect False
    print(sol.isValid("(("))       # expect False (never closed)
    print(sol.isValid(")"))        # expect False (nothing to close)
