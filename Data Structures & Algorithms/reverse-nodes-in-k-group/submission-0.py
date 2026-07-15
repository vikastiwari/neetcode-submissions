class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        times = length // k
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        curr = head
        
        for i in range(times):
            groupFirst = curr
            pre = None
            
            for _ in range(k):
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt

            groupPrev.next = pre
            groupFirst.next=curr
            groupPrev = groupFirst
            
        return dummy.next
