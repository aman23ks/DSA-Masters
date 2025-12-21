# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return True
        
        # Find length of linked list
        length = 0
        curr_head = head
        while curr_head:
            length += 1
            curr_head = curr_head.next
        
        # Find the mid point of the linked list 
        slow = head
        fast = head
        prev = head
         
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            second_start = slow.next
            slow.next = None
        else:
            second_start = slow
            prev.next = None
            
        prev_rev = None
        curr = second_start
        while curr:
            nxt = curr.next
            curr.next = prev_rev
            prev_rev = curr
            curr = nxt
        
        p1 = head
        p2 = prev_rev
        
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True
            
        
