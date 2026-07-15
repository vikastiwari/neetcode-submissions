# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head1=l1
        head2=l2
        
        while l1!=None and l2!=None:
            l1.val = l1.val + l2.val + carry
            carry = l1.val//10
            l1.val = l1.val%10
            l2.val = l1.val
            pre=l1
            l1=l1.next
            l2=l2.next

        if l1 is None and l2 is None:
            if carry>0:
                pre.next = ListNode(carry)
                pre=pre.next
                pre.next=None
            return head1



            return head1

        if l1 is None:
            while l2!=None:
                l2.val= l2.val + carry
                carry = l2.val//10
                l2.val = l2.val%10

                if l2.next is None:
                    if carry>0:
                        l2.next = ListNode(carry)
                        l2=l2.next
                        l2.next=None
                    return head2

                l2=l2.next

        if l2 is None:
            while l1!=None:
                l1.val= l1.val + carry
                carry = l1.val//10
                l1.val = l1.val%10

                if l1.next is None:
                    if carry>0:
                        l1.next = ListNode(carry)
                        l1=l1.next
                        l1.next=None
                    return head1

                l1=l1.next
            






        