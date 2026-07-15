# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # As long as fast and the node AFTER fast exist...
        while fast and fast.next:
            slow = slow.next          # Slow moves 1 step
            fast = fast.next.next     # Fast moves 2 steps

            # If they meet, there is a cycle!
            if slow == fast:
                return True
                
        # If the loop breaks, fast hit the end of the list. No cycle!
        return False
