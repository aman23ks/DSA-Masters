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

        countA = 0
        countB = 0

        count_headA = headA
        count_headB = headB

        while count_headA:
            countA += 1
            count_headA = count_headA.next
        
        while count_headB:
            countB += 1
            count_headB = count_headB.next

        currA = headA
        currB = headB
        while currA and currB:
            if currA == currB:
                return currA
            if countA > countB:
                countA -= 1
                currA = currA.next
            elif countA < countB:
                countB -= 1
                currB = currB.next
            else:
                currA = currA.next
                currB = currB.next
        
        return None