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

# recursive solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(left, head):
            if not head:
                return
            if head.next:
                left.next = ListNode(head.next.val, ListNode(head.val))
                recursive(left.next.next, head.next.next)
            else:
                left.next = ListNode(head.val)
        dummy = ListNode()
        recursive(dummy, head)
        return dummy.next
