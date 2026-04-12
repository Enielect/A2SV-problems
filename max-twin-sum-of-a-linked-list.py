# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse the other half of the list and compare
        slow = fast = head
        max_sum = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the slow
        cur, prev = slow, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        while prev and head:
            max_sum = max(max_sum, prev.val + head.val)
            prev = prev.next
            head = head.next
        return max_sum