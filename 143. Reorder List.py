# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Edge cases
        if head == None or head.next == None or head.next.next == None:
            return head
        #Separate left and right O(n)
        p1 = head
        p2 = head
        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
        right = p1.next
        p1.next = None
        left = head
        #Reverse right O(n)
        p1 = None
        p2 = right
        while p2.next != None:
            #temp inside loop
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        p2.next = p1
        right = p2
        #Combine
        pl1 = left
        pr1 = right
        while pl1 is not None and pr1 is not None:
            #temp inside loop
            pl2 = pl1.next
            pr2 = pr1.next

            pl1.next = pr1
            pr1.next = pl2

            pl1 = pl2
            pr1 = pr2
