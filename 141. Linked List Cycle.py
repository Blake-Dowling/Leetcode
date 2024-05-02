# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p1 = head
        p2 = head
        while p1.next != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next
            if p2.next == None:
                return False
            p2 = p2.next
            if p1 == p2:
                return True
        return False