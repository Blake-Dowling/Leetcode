# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Base case
        if head == None or head.next == None:
            return head
        ### List length is >= 2
        #assign p1 to left-middle or middle
        p1 = head
        p2 = head
        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next
        #Assign right to right-middle
        right = p1.next
        #Break middle connection
        p1.next = None
        left = self.sortList(head)
        right = self.sortList(right)
        #Merge
        p1 = left
        p2 = right
        #O(1) head-reassignment
        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next
        p0 = head
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p0.next = p1
                p0 = p0.next
                p1 = p1.next
            else:
                p0.next = p2
                p0 = p0.next
                p2 = p2.next
        while p1 is not None:
            p0.next = p1
            p0 = p0.next
            p1 = p1.next
        while p2 is not None:
            p0.next = p2
            p0 = p0.next
            p2 = p2.next
        return head