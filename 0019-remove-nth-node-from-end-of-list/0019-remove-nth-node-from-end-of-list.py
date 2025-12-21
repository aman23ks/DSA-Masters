# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_linked_list(self, curr):
        prev = None
        while curr:
            second = curr.next
            curr.next = prev
            prev = curr
            curr = second 

        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        head = self.reverse_linked_list(head)
        
        if n == 1:
            return self.reverse_linked_list(head.next)
        
        p1 = head
        p2 = head
        
        while p2 and p1 and n != 2:
            p2 = p2.next
            p1 = p1.next
            n -= 1
        
        while p2 and n != 0:
            p2 = p2.next
            n-=1

        p1.next = p2

        return self.reverse_linked_list(head)
        