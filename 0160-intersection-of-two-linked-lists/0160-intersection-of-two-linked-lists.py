# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        if headA == headB:
            return headA
        
        currA = headA

        while currA.next:
            currA=currA.next

        currA.next = headA

        slow = headB
        fast = headB
        has_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True 
                break
        
        if not has_cycle:
            currA.next = None
            return None
        
        ptr1 = headB
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        currA.next = None
        return ptr1