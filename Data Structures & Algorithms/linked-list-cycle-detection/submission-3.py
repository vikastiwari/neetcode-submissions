# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        answer = False
        fast =head
        slow =head

        while fast and slow:
            slow=slow.next
            fast = fast.next
            if fast ==None:
                break
            fast = fast.next

            if(slow==fast):
                return True
        return answer
        