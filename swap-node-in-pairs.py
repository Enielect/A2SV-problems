# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur and cur.next and cur.next.next:
            nxt  = cur.next.next
            now = cur.next
            cur.next = nxt
            cur.next.next = ListNode(now.val, nxt.next)
            cur = cur.next.next
        return dummy.next