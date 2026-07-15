class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to hold our new answer list
        dummy = ListNode()
        tail = dummy
        carry = 0
        
        # 2. We keep looping as long as ANY of these three things are true:
        # - l1 still has numbers
        # - l2 still has numbers
        # - We have a carry left over from the last addition
        while l1 is not None or l2 is not None or carry > 0:
            
            # If a list is empty, we just pretend its value is 0!
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # 3. Math time!
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # 4. Attach the new digit to our answer list
            tail.next = ListNode(digit)
            tail = tail.next
            
            # 5. Move l1 and l2 forward (if they aren't already empty)
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            
        # 6. Return dummy.next to skip the fake dummy node!
        return dummy.next
