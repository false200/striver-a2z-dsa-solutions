"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
        
class Solution:
    def searchKey(self, head, key):
        while head:
            if head.val == key: return True
            head = head.next
        return False