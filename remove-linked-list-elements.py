# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        temp = dummy
        while temp and temp.next:
            while temp.next and temp.next.val == val:
                temp.next = temp.next.next
            if temp.next:
                temp = temp.next
        return dummy.next

# optimal solution:

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        cur = head
        
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next
