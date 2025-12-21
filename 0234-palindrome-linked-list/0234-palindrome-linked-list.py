# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1) Find end of first half (slow) using fast/slow pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half starting at slow.next
        second = self._reverse(slow.next)

        # 3) Compare first half and reversed second half
        p1, p2 = head, second
        while p2:
            if p1.val != p2.val:
                # Optional restore before returning
                slow.next = self._reverse(second)
                return False
            p1 = p1.next
            p2 = p2.next

        # 4) Optional: restore list
        slow.next = self._reverse(second)
        return True

    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev