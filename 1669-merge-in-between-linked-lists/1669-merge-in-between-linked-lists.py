# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr_a = list1
        curr_b = list1
        count_a = 0
        count_b = 0
        while curr_a and count_a != a-1:
            curr_a = curr_a.next
            count_a += 1
        while curr_b and count_b != b:
            curr_b = curr_b.next
            count_b += 1
        curr_a.next = list2
        while curr_a.next:
            curr_a = curr_a.next
        
        c = curr_b.next
        curr_b.next = None
        curr_a.next = c
        return list1 

        
