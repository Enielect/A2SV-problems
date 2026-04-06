# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# my initial solution
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # loop through the list twice
        cur = head

        res = ListNode()
        temp = res

        while cur:
            if cur.val < x:
                temp.next = ListNode(cur.val)
                temp = temp.next
            cur = cur.next
            
        cur = head
        while cur:
            if cur.val >= x:
                temp.next = ListNode(cur.val)
                temp = temp.next
            cur = cur.next
        return res.next

# An improved solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # loop through the list twice

        slist, blist = ListNode(), ListNode()
        small, big = slist, blist

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next

        small.next = blist.next
        big.next = None # avoiding stale pointer to head

        return slist.next
