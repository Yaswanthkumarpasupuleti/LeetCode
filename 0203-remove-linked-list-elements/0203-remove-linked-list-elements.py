# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head != None and head.next == None:
            if head.val == val:
                return None
            else:
                return head
        else:
            
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy
            temp = head
            #nextnode = None
            while temp != None:
                if temp.val == val:
                    # if temp != None and prev != None:
                    #     prev.next = temp.next
                    # else:
                    #     prev = None
                    prev.next = temp.next
                    temp=prev
                prev = temp
                temp = temp.next
            return dummy.next


        