# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cycle = False
        while fast != None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        
        if cycle == False:
            return None
        
        slow = head

        if slow == fast:
            return slow

        while slow != fast:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return slow
