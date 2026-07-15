# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        head = lists[0]

        for i in range (1,len(lists)):
            head = self.mergeTwoLists(head,lists[i])    

        return head        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        answer = ListNode()
        head=answer
        
        while list1 !=None and list2 !=None:
            if list1.val<=list2.val:
                head.next=list1
                list1=list1.next
                
            else:
                head.next=list2
                list2=list2.next   

            head=head.next

        if list1==None:
            head.next=list2

        if list2==None:
            head.next=list1             

        return answer.next        







        