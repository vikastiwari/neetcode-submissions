# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        tra=head

        while tra:
            length+=1
            tra=tra.next

        index=0
        target = length - n 

        tra=head
        pre=None
        print(target)
        while  tra:
            if index==target:
                print("index==target", index, target)
                if pre==None:
                    head=head.next
                    break
                pre.next=tra.next
                break 
            index+=1
            pre=tra
            tra=tra.next    
        return head        

        