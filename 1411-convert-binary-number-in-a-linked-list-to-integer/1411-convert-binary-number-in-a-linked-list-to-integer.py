# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = ""
        temp = head
        while temp != None:
            res += str(temp.val)
            temp = temp.next
        res = int(res,2)
        return res
        