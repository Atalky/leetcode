"""
Problem: 2. Add Two Numbers
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/
Tags: Linked List,Math,Recursion
Date: 2026-09-07
Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n))
"""

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = current = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry += v1 + v2
            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

def show(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
print(show(sol.addTwoNumbers(l1, l2)))        # → [7, 0, 8]
