# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        # len = 0
        # temp = head
        
        elif head != None and head.next == None:
            if n == 1:
                return None
            else:
                return head
        elif head != None and head.next != None and head.next.next == None:
            if n == 1:
                head.next = None
            elif n == 2:
                head = head.next
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            slow = dummy
            fast = dummy
            for i in range(n+1):
                fast = fast.next
            
            while fast != None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
        return dummy.next
        