# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        carry = 0
        while l1 or l2:
            workingSum = carry
            if l1:
                workingSum += l1.val
                l1 = l1.next
            if l2:
                workingSum += l2.val
                l2 = l2.next
            out.append(workingSum % 10)
            carry = int(workingSum / 10)
        if carry:
            out.append(carry)
        head = ListNode(out[0], None)
        cur = head
        for i in range(len(out)-1):
            cur.val = out[i]
            cur.next = ListNode(0, None)
            cur = cur.next
        cur.val = out[-1]
        return head
            
            
        