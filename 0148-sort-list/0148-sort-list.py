# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def split_list(self, curr):
        slow, fast = curr, curr
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow
    
    def merge(self, a, b):
        if not a:
            return b
        
        if not b:
            return a
        
        if a.val <= b.val:
            head = tail = a
            a = a.next
        else:
            head = tail = b
            b = b.next
        
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        
        tail.next = a if a else b
        return head


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.split_list(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        