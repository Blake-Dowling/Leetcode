# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head):
        if not head:
            return None
        p1 = head
        p2 = head
        while p1.next != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next
            if p2.next == None:
                return None
            p2 = p2.next
            #Cycle detected
            if p1 == p2:
                l = 1
                p1 = p1.next
                #Count cycle length
                while p1 != p2:
                    l += 1
                    p1 = p1.next
                return l
        return None
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Get cycle length
        l = self.getLength(head)
        if not l:
            return None
        #Find cycle begin
        p1 = head
        p2 = head
        #Move p2 l steps ahead of p1
        while l > 0:
            p2 = p2.next
            l -= 1
        #Single-increment both pointers until meet.
        #This must be cycle begin, because if meet,
        #both must be in cycle, because they are l apart.
        #Both cannot be in cycle at different positions 
        #since then they would not be l apart.
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1