# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            temp = head
            prev = head
            stack = []
            while temp != None:
                if temp.val in stack:
                    prev.next = temp.next
                else:
                    stack.append(temp.val)
                    prev = temp
                temp = temp.next
        return head
        